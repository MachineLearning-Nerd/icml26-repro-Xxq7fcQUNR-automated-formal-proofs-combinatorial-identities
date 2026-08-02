# Claim 1 — LCI-Test result

**Exact live claim:** WZ-LLM solves 34/100 LCI-Test identities versus 9/100 Goedel-Prover-V2 and 1/100 DeepSeek-V3.

## Attempt 1: direct local method fixture — toy
The paper's source releases a concrete WZ/Lean case identity but no LCI-Test files, model weights, Lean tactic, prompts, or baseline inference logs. We therefore executed the source-listed identity
`sum_k (-1)^k C(n,k)m/(m+k)=1/C(m+n,n)` exactly over a finite grid using rational arithmetic. This is **toy evidence**, not an LCI-Test reproduction.

`python src/claim1_wz_identity_toy.py --out outputs/claim1_wz_identity_toy --max-n 12 --max-m 12`

The direct and recurrence checks pass in all 156 cells; a corrupted-sign control fails. Artifacts and hashes: `outputs/claim1_wz_identity_toy/`.

**Verdict: toy.** It cannot establish the 34/100 benchmark comparison.
