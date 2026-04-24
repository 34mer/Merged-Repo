# 19. Theorem dependency graph

Status: OPERATIONS / MATH AUTHORITY

This file externalizes the minimum dependency graph that must otherwise stay in the model's head.

## Dependency graph (compact)

### Baseline layer
- B1 Cosmohedron exact baseline [U-EXACT]
- B2 Associahedron exact baseline [U-EXACT]
- B3 Amplituhedron m=1 exact baseline [U-EXACT]
- B4 Surfaceology exact local baseline [U-EXACT]
- B5 Cross-family conclusion before rebuild [U-EXACT]

### Mathematical spine
- E1 Static residue base [M-EXACT]
  - depends on: accepted static positive-geometry reading in-thread
- E2 Intrinsic root-bundle layer [M-EXACT]
  - depends on: E1
- E3 Local A2 quarter-turn transport [M-EXACT]
  - depends on: E2
- E4 Finite positive-Grassmannian top-cell closure on A, D4, E6 [M-EXACT]
  - depends on: E1, E2, E3, finite-type top-cell branch derivations in-thread
- E5 Support-node orbit law [M-EXACT]
  - depends on: E4 plus support/orbit reduction in-thread
- E6 Parabolic residue recursion [M-EXACT]
  - depends on: E4, E5
- E7 Surfaceology next exact frontier [U-EXACT + OPEN]
  - depends on: B4 and absence of global footing result

### Generated continuations
- G1 Additive/formal branches [GEN]
  - depends on: E1–E3 as formal seed, but not source-backed
- G2 Abstract D_n extension [GEN]
  - depends on: E4, E5, E6 as formal continuation, not exact sourced branch
- G3 CRBSM regime class [GEN]
  - depends on: E1–E6 plus BRIDGE translation; not an exact mathematical consequence

### Provisional translation layer
- P1 Support survival [BRIDGE]
  - depends on: E2, E3, E4 interpreted toward realization
- P2 Boundary-primary disclosure [BRIDGE]
  - depends on: E1, E4 interpreted toward realization
- P3 Apparatus coupling [BRIDGE]
  - depends on: P1, P2
- P4 Persistent relay/support ledger [BRIDGE / SUSPECT]
  - depends on: P1 interpreted through an older machine frame; must be re-derived or dropped

## Safe use rule
If a claim depends on any GEN or BRIDGE node, it must not be restated later as if it depended only on E1–E7.

## Immediate consequence
The exact authority chain currently terminates at:
- static residue base
- intrinsic root-bundle layer
- local A2 quarter-turn transport
- finite top-cell closure on A / D4 / E6
- support-node orbit law
- parabolic residue recursion
- surfaceology as next exact frontier

Everything else is either generated continuation or provisional translation.
