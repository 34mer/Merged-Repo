from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from .baseline import benchmark
from .boundary_models import hydrogen_boundary, unfold


def verify_hydrogen(levels: int = 10) -> Primitive:
    boundary = hydrogen_boundary()
    target = benchmark(levels)
    predicted = unfold(boundary, levels)
    errors = [relative_error(predicted["ionization_energy_ev"], target["ionization_energy_ev"])]
    for p, t in zip(predicted["levels"], target["levels"]):
        errors.append(relative_error(p["energy_ev"], t["energy_ev"]))
        errors.append(0.0 if p["degeneracy"] == t["degeneracy"] else 1.0)
    errors.append(relative_error(predicted["lyman_alpha_ev"], target["lyman_alpha_ev"]))
    errors.append(relative_error(predicted["balmer_alpha_ev"], target["balmer_alpha_ev"]))
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="hydrogen",
        status="HYDROGEN BOUNDARY OBJECT VERIFIED" if score >= 0.999999 else "HYDROGEN VERIFICATION FAILED",
        score=score,
        metrics={"max_error": max(errors), "mean_error": sum(errors) / len(errors), "levels": levels},
    )
    return Primitive(
        name="hydrogen_primitive",
        version="v0.1",
        layer="hydrogen",
        boundary_object=boundary,
        observables=predicted,
        verification=report.to_dict(),
    )
