# Thread Continuity Architecture

Purpose: preserve the research state of the long thread as a usable continuation surface, without pretending that every item is solved or theorem-certified.

This file corrects an earlier narrow upload. The first patch uploaded an R2/R3 comparison. The second patch uploaded an R1-R14 ledger. That is still not the full continuity architecture. The missing layer is an inventory of packages, registries, comparators, source coverage, and next actions needed to carry the whole project into a fresh thread or tool environment.

## Current top-level object

Build a checked, source-bound, computable map:

positive-geometry / amplitudes / cosmological-geometry families -> structural rows -> realization-class discriminators

before any substrate or engineering commitment.

## Already present in repo

- R1-R14 discriminator ledger: `research_ledger/R1_R14_DISCRIMINATOR_LEDGER.md` and `.json`
- Realization-class pair matrix: `research_ledger/REALIZATION_CLASS_MATRIX.md`
- Proof/checker obligations: `research_ledger/PROOF_OBLIGATIONS.md`
- R2/R3 typed comparison slice in `pg_pipeline/`
- Exact-work and Lean-related scaffold under `exact_work/`

## Missing or only partially present

The following are not just filenames. They are project functions that need to exist somewhere in the repo.

| Package function | Current state | Required role |
|---|---|---|
| Paper/source ledger | MISSING | Paper-by-paper map of all uploaded sources, with what each contributes and what claims it can support. |
| Extraction ledger | PARTIAL | Tracks what has been extracted from each paper and what remains. |
| Row catalog | PRESENT/PARTIAL | R1-R14 exists, but row predicates need source binding and typed definitions. |
| Coverage matrix | PARTIAL | Current pair matrix exists, but not full row x family coverage. |
| Support ledger | PARTIAL | Source-backed rows are tagged, but top support rows and support chains are not separated. |
| Caution ledger | PARTIAL | OPEN/DEFICIT tags exist, but caution claims are not separately indexed. |
| Survivor assessment | PARTIAL | Some survivor rows are stated, but no full survivor/failure assessment exists. |
| Comparator packages | PARTIAL | R2/R3 exists; other comparator packages are mostly missing. |
| Surfaceology comparator | PARTIAL/MISSING | Surfaceology is represented by `S`, but not expanded as a full comparator package. |
| Frontier notes | MISSING | Needs record of live uncertain boundary between source results, generated extensions, and real open math. |
| Extraction package | MISSING | Needs cold-start continuation package for a fresh thread. |
| Next action register | PARTIAL | Proof obligations exist, but not prioritized as work objects. |
| Growth status registry | MISSING | Needs status of each subsystem: source, extraction, checker, comparator, solver/MCP, repo. |
| Project hierarchy synthesis | MISSING | Needs hierarchy of object, methods, ledgers, comparators, substrate boundary, and non-commitment rule. |
| Failure-mode registry | MISSING | Needs explicit list of known model/repo failure modes. |
| Tool/MCP registry | MISSING | Needs planned math organs: Lean, Z3, Sage, polymake, artifact store, source retriever. |

## Paper/source ledger required shape

Each paper record must include:

- `paper_id`
- title
- family/classes touched
- source-backed claims
- extracted rows supported
- caution notes
- comparator relevance
- formalization targets

The uploaded source corpus includes amplituhedron, scattering forms/associahedron, binary/sign-flip amplituhedron, momentum amplituhedron, loop momentum amplituhedron, cosmohedra, combinatorics of cosmohedron, surfaceology/curve-integral papers, scalar-scaffolded gluons, hidden zeros, Wilson-loop positivity, and colored Yukawa surfaceology.

## Extraction ledger required shape

Each extraction item must include:

- source paper
- extracted object
- exact/source status
- row(s) affected
- class/family affected
- current verdict
- missing formalization
- next checker target

## Comparator packages required

At minimum:

1. `GAssoc` vs `C` equality-layer comparator: PRESENT/PARTIAL.
2. `A` vs `C` local-move/nesting comparator: PARTIAL.
3. `M1` vs `C` descent/local-move comparator: PARTIAL.
4. `A` vs `M1` shared descent but representation-distinct comparator: OPEN.
5. `S` vs `A/M1/C` surfaceology comparator: MISSING.
6. `PGfinite` vs `S` exact finite branch vs surfaceology branch comparator: PARTIAL.
7. Scalar-scaffolded / hidden-zero / transmutation comparator: MISSING.
8. Momentum-amplituhedron / loop-momentum-amplituhedron comparator: MISSING.
9. Wilson-loop positive/negative geometry comparator: MISSING.
10. Colored-Yukawa surfaceology extension comparator: MISSING.

## Survivor assessment required shape

Rows must be split into:

- `survives_across_multiple_families`
- `family_specific_candidate`
- `ordered_specialization_candidate`
- `generated_only`
- `failed_or_absent`
- `open_deficit`

Current provisional survivor state:

- R1 survives as a shared lower layer.
- R9-R12 survive across `GAssoc` and `C` but do not separate them.
- R13 separates `GAssoc` and `C` at thread-supported level.
- R2/R3 are candidate cosmohedron-specific separators against `A` and `M1`.
- R14 is the open deficit.

## Caution ledger required shape

Claims that must not be silently promoted:

- R13 is thread-supported, not Lean-certified.
- R14 is open/deficit, not solved.
- Surfaceology is not on equal global footing yet.
- CRBSM is generated-only, not the object.
- Passing a pipeline slice is not mathematical proof.
- Similarity/clustering is not realization-class equivalence.
- Symbolic scaffolds are not solved math.
- Source-backed extraction, internal derivation, and generated extension must remain separate.

## Project hierarchy synthesis

1. Object: source-bound positive-geometry family extraction and realization-class discrimination.
2. Source layer: uploaded papers and exact-work artifacts.
3. Extraction layer: paper -> object -> row predicate.
4. Comparator layer: family/class pair comparisons.
5. Checker layer: Python/Sage/Z3/Lean where appropriate.
6. Ledger layer: source/status/proof obligations.
7. Repo/MCP layer: execution and continuity tooling.
8. Substrate boundary: no substrate commitment from these rows unless mathematically forced by later work.

## Next action register

1. Build paper/source ledger for all uploaded papers.
2. Build extraction ledger from papers to rows.
3. Build full row x family coverage matrix.
4. Expand surfaceology comparator package.
5. Separate support ledger and caution ledger.
6. Convert survivor assessment into machine-readable form.
7. Add failure-mode registry.
8. Add tool/MCP registry.
9. Convert key rows into typed predicates.
10. Add checker targets for R1, R2, R3, R12, R13, R14.

## Growth status registry

| Subsystem | Status |
|---|---|
| Source corpus | uploaded, not fully paper-ledgered |
| R1-R14 row ledger | present, not source-bound enough |
| Class matrix | present, partial |
| Comparator packages | only R2/R3 properly started |
| Surfaceology | underrepresented |
| Proof/checker layer | obligations present, implementation mostly open |
| MCP/tool plan | conceptual, not wired |
| Repo continuity | improving, not complete |
| Math foundation | not solved; must be checked externally |

## Immediate correction

The repo must not be treated as complete just because R1-R14 exists. The missing continuity architecture is now identified here. Future patches should instantiate the missing package functions, starting with paper/source ledger and extraction ledger.
