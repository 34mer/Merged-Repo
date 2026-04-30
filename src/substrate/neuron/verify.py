from __future__ import annotations

from substrate.core import Primitive, VerificationReport, relative_error, score_from_errors
from substrate.channel.verify import verify_channel
from .baseline import neuron_benchmark
from .boundary_models import neuron_boundary, unfold


def verify_neuron() -> Primitive:
    na = verify_channel("sodium")
    k = verify_channel("potassium")
    boundary = neuron_boundary()
    target = neuron_benchmark()
    predicted = unfold(boundary)
    errors = [
        relative_error(predicted["pulse_response"]["spike_count"], target["pulse_response"]["spike_count"], floor=1.0),
        relative_error(predicted["pulse_response"]["final_energy"], target["pulse_response"]["final_energy"]),
    ]
    for p, t in zip(predicted["fi_curve"]["rows"], target["fi_curve"]["rows"]):
        errors.append(relative_error(p["spike_count"], t["spike_count"], floor=1.0))
    score = score_from_errors(errors)
    report = VerificationReport(
        layer="neuron",
        status="SINGLE NEURON PROCESS PRIMITIVE VERIFIED" if score >= 0.999 else "NEURON VERIFICATION FAILED",
        score=score,
        metrics={"spike_count": predicted["pulse_response"]["spike_count"], "max_error": max(errors)},
    )
    return Primitive(
        name="single_neuron_process_primitive",
        version="v0.1",
        layer="neuron",
        boundary_object=boundary,
        observables=predicted,
        verification=report.to_dict(),
        parents=[na.hash, k.hash],
    )
