from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from substrate.hydrogen.verify import verify_hydrogen
from .baseline import morse_curve
from .boundary_models import h2_boundary, unfold


def verify_h2() -> Primitive:
    hydrogen = verify_hydrogen()
    boundary = h2_boundary()
    target = morse_curve()
    predicted = unfold(boundary)
    errors = [
        relative_error(predicted["bond_length_angstrom"], target["bond_length_angstrom"]),
        relative_error(predicted["binding_energy_ev"], target["binding_energy_ev"]),
        relative_error(predicted["vibrational_frequency_cm"], target["vibrational_frequency_cm"]),
    ]
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="molecule",
        status="MOLECULE BOUNDARY OBJECT VERIFIED" if score >= 0.999 else "MOLECULE VERIFICATION FAILED",
        score=score,
        metrics={"max_error": max(errors), "molecule": "H2"},
    )
    return Primitive(
        name="molecule_primitive",
        version="v0.1",
        layer="molecule",
        boundary_object=boundary,
        observables=predicted,
        verification=report.to_dict(),
        parents=[hydrogen.hash],
    )
