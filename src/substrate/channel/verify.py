from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from substrate.membrane.verify import verify_membrane
from .baseline import channel_benchmark
from .boundary_models import channel_boundary, unfold


def verify_channel(kind: str = "sodium") -> Primitive:
    parent = verify_membrane()
    boundary = channel_boundary(kind)
    target = channel_benchmark(kind)
    predicted = unfold(boundary)
    errors = []
    for key in ["g_max", "e_rev_mv", "v_half_mv", "slope_mv", "recovery_ms"]:
        errors.append(relative_error(predicted["parameters"][key], target["parameters"][key]))
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="channel",
        status="CHANNEL PRIMITIVE VERIFIED" if score >= 0.999 else "CHANNEL VERIFICATION FAILED",
        score=score,
        metrics={"kind": kind, "max_error": max(errors)},
    )
    return Primitive(
        name=f"{kind}_channel_primitive",
        version="v0.1",
        layer="channel",
        boundary_object=boundary,
        observables=predicted,
        verification=report.to_dict(),
        parents=[parent.hash],
    )
