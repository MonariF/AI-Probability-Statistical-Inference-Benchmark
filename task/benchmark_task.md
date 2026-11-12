# Benchmark Task 003: Binomial Probability and Exact Statistical Inference

A process is claimed to have success probability `p0 = 0.25`. In `n = 40` independent trials, `x = 16` successes are observed.

## Candidate instructions
Use Python, NumPy and SciPy to:
1. Define `X ~ Binomial(40, 0.25)` under the null.
2. Calculate `P(X >= 16)` accurately. For a discrete distribution, avoid off-by-one tail errors.
3. Conduct the exact two-sided binomial test of `H0: p=0.25` against `H1: p != 0.25`, at alpha 0.05.
4. Calculate a 95% Clopper-Pearson exact confidence interval.
5. Estimate `P(X >= 16)` by Monte Carlo simulation using the null probability 0.25, at least 200,000 replicates and a fixed seed.
6. Compare the simulation estimate with the analytical probability.
7. Explain the difference between the upper-tail probability and the two-sided exact-test p-value.
8. Report code, sample proportion, p-value, interval, simulation settings and conclusion.

## Critical errors
- Using `cdf(16)` for `P(X >= 16)` instead of `sf(15)`.
- Reporting the upper-tail probability as the two-sided p-value.
- Simulating under the observed proportion 0.40 instead of null probability 0.25.
- Using an unseeded simulation while claiming reproducibility.
- Calling a Wald interval an exact interval.
- Giving a conclusion inconsistent with the exact test.
