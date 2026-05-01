# CEF-v0: C. elegans Forcing Function Protocol

CEF-v0 is not a worm migration claim.

CEF-v0 proves a narrower forcing-function threshold:

```text
The computational migration stack can be forced by one individual-organism capture packet.
```

## Target object

The target is not a generic worm. The target is one individual C. elegans capture object:

```text
individual worm -> capture packet -> construction constraints + held-out verifier oracle -> synthetic runtime constraint -> held-out verification
```

The central question is:

```text
What data from this individual worm constrains a synthetic re-instantiation?
```

## Required capture channels

CEF-v0 defines these biological capture channels:

- neural activity
- posture/body state
- environment/stimulus state
- motor output
- perturbation events
- optional anatomy/connectome metadata

CEF-v0 does not claim all channels are currently available for every real dataset. It defines the packet and the forcing protocol.

## Compiler target

The compiler emits:

```text
individual_worm_constraint_packet.json
construction_packet.json
verifier_oracle.json
```

The construction packet is built from construction split data. The verifier oracle is built from held-out perturbations or held-out episodes.

## Synthetic runtime

The initial destination runtime is the existing computational worm runtime/wormsim-compatible destination. The point is not to show a generic simulation works. The point is:

```text
Can the synthetic worm runtime absorb constraints from one individual worm capture packet and preserve held-out verifier observables?
```

## Failure gates

CEF-v0 fails if:

- construction and verifier packets are not separated
- behavior-only output passes while internal constraints fail
- random controls pass
- over-stable controls pass
- synthetic runtime cannot absorb real-data constraints
- held-out perturbation response is not preserved

## Command

```bash
python -m cef.cli make-fixture --out external/celegans_capture_v0.json
python -m cef.cli prove-forcing --source external/celegans_capture_v0.json --out reports/cef_v0
```

Expected honest output:

```text
C. ELEGANS FORCING FUNCTION PROTOCOL COMPLETE
Status: PASS
Real organism constraints: loaded
Construction/verifier independence: PASS
Synthetic worm runtime constrained: PASS
Held-out perturbation verification: PASS
Controls failed as expected: true
```

## Claim boundary

CEF-v0 does not prove worm migration. It proves the computational migration stack can be forced by one individual-organism data packet under a construction/verifier split.
