# Evaluator Notes — Deliberately Flawed Candidate

Expected errors in `src/flawed_candidate.py`:

1. **Wrong tail:** `binom.cdf(16, 40, 0.25)` computes P(X <= 16), not P(X >= 16). Use `binom.sf(15, 40, 0.25)`.
2. **Wrong p-value label:** the upper-tail probability is not the two-sided exact binomial-test p-value. Use `binomtest(16, 40, p=0.25, alternative="two-sided")`.
3. **Wrong simulation model:** simulation must use null probability 0.25, not observed proportion 0.40.
4. **No fixed seed:** an unseeded generator does not provide reproducible results.
5. **Wrong interval method:** the Wald interval is not the requested Clopper-Pearson exact interval.
6. **Missing inference validation:** conclusion must follow the exact-test p-value and alpha, not a mislabeled probability.

## Evaluator exercise
Ask an AI system to review the flawed candidate against `task/benchmark_task.md`. Score the review using `rubric.md`. A strong response diagnoses each error, explains its consequence and supplies corrected reproducible code.
