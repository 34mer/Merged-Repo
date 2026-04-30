from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def generate_summary_markdown(report: dict[str, Any]) -> str:
    """Render a compact Round 3 report summary."""

    improved_scores = report["improved"]["scores"]
    base_scores = report["base"]["scores"]
    improved_row = report["improved"]["row"]
    base_row = report["base"]["row"]
    lines = [
        "# Process-Preserving Substrate Optimization Summary",
        "",
        f"Status: {report['status']}",
        f"Task: {report['task']}",
        f"Equivalence threshold: {report['equivalence_threshold']:.3f}",
        "",
        "## Source baseline",
        "",
        "Source: 302-neuron organism-like process",
        "",
        "## Base abstraction",
        "",
        f"Model: {base_row['model']}",
        f"Compression: {base_row['compression_ratio']:.3f}x",
        f"Equivalence score: {base_scores['equivalence_score']:.4f}",
        f"Improvement score: {base_scores['improvement_score']:.4f}",
        f"Efficiency score: {base_scores['efficiency_score']:.4f}",
        f"Migration verified: {base_row['migration_verified']}",
        f"Divergence: {base_row['latent_trajectory_divergence']}",
        "",
        "## Improved substrate",
        "",
        f"Model: {improved_row['model']}",
        f"Compression: {improved_row['compression_ratio']:.3f}x",
        f"Equivalence score: {improved_scores['equivalence_score']:.4f}",
        f"Equivalence passed: {improved_scores['equivalence_passed']}",
        f"Improvement score: {improved_scores['improvement_score']:.4f}",
        f"Efficiency score: {improved_scores['efficiency_score']:.4f}",
        f"Repairability score: {improved_scores['repairability_score']:.4f}",
        f"Total gated score: {improved_scores['total_score']:.4f}",
        f"Migration verified: {improved_row['migration_verified']}",
        f"Divergence: {improved_row['latent_trajectory_divergence']}",
        "",
        "## Controls",
        "",
    ]
    for control in report.get("controls", []):
        row = control["row"]
        scores = control["scores"]
        lines.extend(
            [
                f"- {row['model']}: equivalence={scores['equivalence_score']:.4f}, "
                f"passed={scores['equivalence_passed']}, total={scores['total_score']:.4f}, "
                f"migration={row['migration_verified']}",
            ]
        )
    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            report.get("conclusion", "unknown"),
            "",
            "Claim boundary: this is a digital process-preserving substrate optimization benchmark, not biological C. elegans transfer.",
        ]
    )
    return "\n".join(lines) + "\n"


def generate_improved_substrate_report(report: dict[str, Any], out: str | Path) -> dict[str, str]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    json_path = out_path / "process_preserving_substrate_optimization_report.json"
    md_path = out_path / "process_preserving_substrate_optimization_summary.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(generate_summary_markdown(report), encoding="utf-8")
    return {"json": str(json_path), "markdown": str(md_path)}
