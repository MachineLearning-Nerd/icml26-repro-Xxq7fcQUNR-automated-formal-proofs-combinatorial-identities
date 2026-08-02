# Reproduction: Automated Formal Proofs of Combinatorial Identities via Wilf–Zeilberger Guidance and LLMs

Clean-room local CPU/GPU reproduction workspace for ICML 2026 submission 439 (`Xxq7fcQUNR`). Exact live claims and immutable source pins are in `contract/` and `evidence/source/`.

Compute policy: local CPU/local GPU only; no HF cpu-upgrade, Jobs, paid, or remote compute.

## Initial source feasibility
The pinned arXiv source archive (`2605.04472`) contains manuscript/figure assets but no released benchmark, model checkpoint, training recipe, Lean project, or execution log. Claim 1 therefore requires a direct local executable-proof/benchmark recovery or clean-room finite protocol before any outcome.

## Checks
```bash
(cd evidence/source && sha256sum -c SHA256SUMS)
python3 -m pytest -q
```
