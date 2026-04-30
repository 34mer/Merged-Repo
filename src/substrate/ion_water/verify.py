from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from substrate.molecule.verify import verify_h2
from .baseline import benchmark
from .boundary_models import ion_water_boundary, unfold


def verify_ion_water() -> Primitive:
    parent = verify_h2()
    boundary = ion_water_boundary()
    target = benchmark()
    predicted = unfold(boundary)
    errors: list[float] = []
    for ion, target_values in target["ions"].items():
        pred = predicted["ions"][ion]
        errors.append(0.0 if pred["charge"] == target_values["charge"] else 1.0)
        errors.append(relative_error(pred["diffusion_um2_ms"], target_values["diffusion_um2_ms"]))
        errors.append(relative_error(pred["hydration_energy_kj_mol"], target_values["hydration_energy_kj_mol"]))
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="ion_water",
        status="ION WATER PRIMITIVE VERIFIED" if score >= 0.999 else "ION WATER VERIFICATION FAILED",
        score=score,
        metrics={"max_error": max(errors), "ions": list(target["ions"].keys())},
    )
    return Primitive("ion_water_primitive", "v0.1", "ion_water", boundary, predicted, report.to_dict(), [parent.hash])
