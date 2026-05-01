# CEF-v0.3 Window-Level Dynamics and Robustness

## Result label

CEF-v0.3 is a real-data forcing upgrade, not a migration proof.

- Real Dryad ingestion: PASS
- Oracle leakage: false
- Controls failed as expected: true
- Leave-one-window-out robustness: PARTIAL
- Final status: real-data forcing with ranked invariant-gap failure localization

## What changed from CEF-v0.2

CEF-v0.2 used scalar window means and a low-order construction-only projection. CEF-v0.3 adds window-level dynamics and transition observables so failures can be localized by feature and held-out window.

New dynamic observables include:

- neural_slope
- neural_variance
- neural_peak
- neural_lagged_response
- posture_slope
- motor_slope
- perturbation_response_peak
- perturbation_response_auc
- perturbation_response_decay
- population_activity_dispersion
- previous_stimulus_mean
- delta_stimulus
- previous_neural_mean
- delta_neural
- previous_perturbation_response
- delta_perturbation_response

The compiler now derives numeric observable features from the capture instead of hard-coding only the six CEF-v0.2 scalar means. The runtime fits construction-only ridge models over named driver vectors and remains verifier-blind.

## Real Dryad runs

The v0.3 Dryad import supports 12, 18, and 24 windows. All runs used the same real Dryad copper-boundary H5 file and evaluated formal leave-one-window-out robustness.

| Windows | Status | Passed LOO cases | Failed LOO cases | Oracle leakage | Controls failed |
|---:|---|---:|---:|---|---|
| 12 | PARTIAL | 0 | 12 | false | true |
| 18 | PARTIAL | 0 | 18 | false | true |
| 24 | PARTIAL | 0 | 24 | false | true |

## Interpretation

CEF-v0.3 successfully sharpens the forcing object. It does not make the real-data result pass by weakening criteria. Instead, it exposes a stronger invariant gap: window-specific neural and perturbation-response dynamics remain unpredictable under leave-one-window-out verification.

The top ranked gaps repeatedly involve neural population features and perturbation response features, including neural_peak, neural_mean, previous_neural_mean, neural_lagged_response, and perturbation_response.

## Correct conclusion

CEF-v0.3 has crossed from scalar split-ablation into real-data robustness failure analysis. The system now identifies which dynamic invariants fail under verifier-blind held-out windows.

Do not call this worm migration. The correct label is:

```text
CEF-v0.3 real-data window dynamics: implemented
Real Dryad ingestion: PASS
Formal LOO robustness: PARTIAL / FAIL
Primary invariant gap: neural and perturbation-response dynamics
Status: real-data forcing, not migration
```
