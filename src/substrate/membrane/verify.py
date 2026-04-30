from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from substrate.ion_water.verify import verify_ion_water
from .baseline import membrane_benchmark
from .boundary_models import membrane_boundary, unfold


def verify_membrane() -> Primitive:
    parent = verify_ion_water()
    boundary = membrane_boundary()
    target = membrane_benchmark()
    predicted = unfold(boundary)
    errors = [
        relative_error(predicted["resting_potential_mv"], target["resting_potential_mv"]),
        relative_error(predicted["tau_ms"], target["tau_ms"]),
        relative_error(predicted["capacitance_uF_cm2"], target["capacitance_uF_cm2"]),
    ]
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="membrane",
        status="MEMBRANE PRIMITIVE VERIFIED" if score >= 0.999 else "MEMBRANE VERIFICATION FAILED",
        score=score,
        metrics={"max_error": max(errors), "resting_potential_mv": predicted["resting_potential_mv"]},
    )
    return Primitive(
        name="membrane_primitive",
        version="v0.1",
        layer="membrane",
        boundary_object=boundary,
        observables=predicted,
        verification=report.to_dict(),
        parents=[parent.hash],
    )
