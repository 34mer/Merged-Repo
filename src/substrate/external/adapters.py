from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from substrate.core import stable_hash, write_json
from .ephys import EPHYS_SCHEMA
from .metrics import detect_spikes


def _coerce_float(value: Any, default: float = 0.0) -> float:
    if value is None or value == "":
        return default
    return float(value)


def _finalize_dataset(source_name: str, cell_id: str, protocols: list[dict[str, Any]], metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    if not protocols:
        raise ValueError("No protocols found in external electrophysiology source")
    normalized = []
    for idx, protocol in enumerate(protocols):
        voltage = [float(v) for v in protocol["voltage_mv"]]
        dt_ms = float(protocol["dt_ms"])
        split = protocol.get("split") or ("train" if idx % 3 != 2 else "heldout")
        normalized.append(
            {
                "protocol_id": str(protocol.get("protocol_id", f"protocol_{idx}")),
                "split": split,
                "current_uA": float(protocol.get("current_uA", 0.0)),
                "duration_ms": float(protocol.get("duration_ms", len(voltage) * dt_ms)),
                "dt_ms": dt_ms,
                "pulse_start_ms": float(protocol.get("pulse_start_ms", 0.0)),
                "pulse_end_ms": float(protocol.get("pulse_end_ms", len(voltage) * dt_ms)),
                "voltage_mv": voltage,
                "spike_times_ms": protocol.get("spike_times_ms") or detect_spikes(voltage, dt_ms),
            }
        )
    dataset = {
        "schema": EPHYS_SCHEMA,
        "source_name": source_name,
        "cell_id": str(cell_id),
        "metadata": metadata or {},
        "protocols": normalized,
    }
    dataset["source_hash"] = stable_hash(dataset)
    return dataset


def import_ephys_csv(
    source: str | Path,
    out: str | Path,
    source_name: str,
    cell_id: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Import row-per-sample CSV into substrate-external-ephys-v1.

    Required columns:
      protocol_id, voltage_mv

    Optional columns:
      split, t_ms, dt_ms, current_uA, current_pA, duration_ms,
      pulse_start_ms, pulse_end_ms
    """

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    with Path(source).open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "protocol_id" not in reader.fieldnames or "voltage_mv" not in reader.fieldnames:
            raise ValueError("CSV must include protocol_id and voltage_mv columns")
        for row in reader:
            groups[str(row["protocol_id"])].append(row)

    protocols: list[dict[str, Any]] = []
    for protocol_id, rows in sorted(groups.items()):
        voltage = [_coerce_float(row.get("voltage_mv")) for row in rows]
        times = [_coerce_float(row.get("t_ms"), float(idx)) for idx, row in enumerate(rows)]
        if len(times) > 1:
            dt_ms = times[1] - times[0]
        else:
            dt_ms = _coerce_float(rows[0].get("dt_ms"), 1.0)
        current_uA = _coerce_float(rows[0].get("current_uA"), None) if rows[0].get("current_uA") not in (None, "") else _coerce_float(rows[0].get("current_pA"), 0.0) / 1_000_000.0
        protocols.append(
            {
                "protocol_id": protocol_id,
                "split": rows[0].get("split") or None,
                "current_uA": current_uA,
                "duration_ms": _coerce_float(rows[0].get("duration_ms"), len(voltage) * dt_ms),
                "dt_ms": dt_ms,
                "pulse_start_ms": _coerce_float(rows[0].get("pulse_start_ms"), 0.0),
                "pulse_end_ms": _coerce_float(rows[0].get("pulse_end_ms"), len(voltage) * dt_ms),
                "voltage_mv": voltage,
            }
        )
    dataset = _finalize_dataset(source_name, cell_id, protocols, metadata={"adapter": "csv", **(metadata or {})})
    write_json(out, dataset)
    return dataset


def import_allen_sweep_json(source: str | Path, out: str | Path) -> dict[str, Any]:
    """Import an AllenSDK-style exported sweep JSON into the adhesion schema.

    Expected shape:
      {
        "cell_id": "...",
        "source_name": "allen_cell_types_export",
        "metadata": {...},
        "sweeps": [
          {
            "sweep_number": 1,
            "split": "train" | "heldout",
            "current_pA" or "current_uA": number,
            "dt_ms": number,
            "voltage_mv" or "response_mv": [...],
            "stimulus_start_ms": number,
            "stimulus_end_ms": number
          }
        ]
      }
    """

    payload = json.loads(Path(source).read_text(encoding="utf-8"))
    protocols: list[dict[str, Any]] = []
    for idx, sweep in enumerate(payload.get("sweeps", [])):
        voltage = sweep.get("voltage_mv", sweep.get("response_mv"))
        if voltage is None:
            raise ValueError(f"Sweep {idx} missing voltage_mv/response_mv")
        current_uA = float(sweep.get("current_uA", float(sweep.get("current_pA", 0.0)) / 1_000_000.0))
        dt_ms = float(sweep.get("dt_ms", 1000.0 / float(sweep.get("sampling_rate_hz", 1000.0))))
        protocols.append(
            {
                "protocol_id": str(sweep.get("protocol_id", f"sweep_{sweep.get('sweep_number', idx)}")),
                "split": sweep.get("split") or None,
                "current_uA": current_uA,
                "duration_ms": float(sweep.get("duration_ms", len(voltage) * dt_ms)),
                "dt_ms": dt_ms,
                "pulse_start_ms": float(sweep.get("stimulus_start_ms", sweep.get("pulse_start_ms", 0.0))),
                "pulse_end_ms": float(sweep.get("stimulus_end_ms", sweep.get("pulse_end_ms", len(voltage) * dt_ms))),
                "voltage_mv": [float(v) for v in voltage],
            }
        )
    dataset = _finalize_dataset(
        str(payload.get("source_name", "allen_cell_types_export")),
        str(payload.get("cell_id", payload.get("specimen_id", "unknown_cell"))),
        protocols,
        metadata={"adapter": "allen_sweep_json", **dict(payload.get("metadata", {}))},
    )
    write_json(out, dataset)
    return dataset


def import_nwb_file(source: str | Path, out: str | Path, source_name: str = "nwb_export", cell_id: str = "unknown_cell") -> dict[str, Any]:
    """Best-effort NWB importer using optional pynwb.

    This intentionally remains optional so CI does not depend on large neurodata
    packages. For reliable production use, export sweeps with AllenSDK/DANDI into
    the JSON or CSV adapters above, or install pynwb and inspect the generated file.
    """

    try:
        from pynwb import NWBHDF5IO  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("import-nwb requires optional dependency pynwb. Install pynwb or export to JSON/CSV.") from exc

    protocols: list[dict[str, Any]] = []
    with NWBHDF5IO(str(source), "r", load_namespaces=True) as io:  # pragma: no cover - optional dependency
        nwb = io.read()
        acquisitions = list(nwb.acquisition.items())
        for idx, (name, series) in enumerate(acquisitions):
            data = getattr(series, "data", None)
            if data is None:
                continue
            voltage = [float(v) for v in data[:]]
            rate = float(getattr(series, "rate", 1000.0) or 1000.0)
            dt_ms = 1000.0 / rate
            protocols.append(
                {
                    "protocol_id": str(name),
                    "split": "train" if idx % 3 != 2 else "heldout",
                    "current_uA": 0.0,
                    "duration_ms": len(voltage) * dt_ms,
                    "dt_ms": dt_ms,
                    "pulse_start_ms": 0.0,
                    "pulse_end_ms": len(voltage) * dt_ms,
                    "voltage_mv": voltage,
                }
            )
    dataset = _finalize_dataset(source_name, cell_id, protocols, metadata={"adapter": "nwb_pynwb", "source_file": str(source)})
    write_json(out, dataset)
    return dataset
