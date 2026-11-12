# Scoring Rubric — Benchmark Task 003

Total: 100 points.

| Criterion | Points | Full-credit standard |
|---|---:|---|
| Probability model and notation | 10 | Correct binomial model and assumptions. |
| Analytical upper-tail probability | 15 | Correctly computes P(X >= 16), e.g. `binom.sf(15, 40, 0.25)`. |
| Exact hypothesis test | 15 | Correct two-sided exact binomial test and p-value. |
| Exact confidence interval | 15 | 95% Clopper-Pearson interval, correctly identified. |
| Monte Carlo design | 15 | Simulates under p0, at least 200,000 replicates, fixed seed. |
| Numerical validation | 10 | Compares simulation with analytical tail probability and accounts for simulation error. |
| Statistical interpretation | 10 | Distinguishes tail probability, p-value and confidence interval; valid decision. |
| Reproducibility and communication | 10 | Executable code, assumptions, settings and clear reporting. |

## Critical errors
Major deductions for incorrect discrete-tail indexing, confusing a one-sided tail with a two-sided p-value, simulating under the wrong probability, claiming reproducibility without a fixed seed, or mislabelling a Wald interval as exact.

## Score bands
90–100 Excellent; 75–89 Good; 60–74 Borderline; 40–59 Poor; 0–39 Unacceptable.
