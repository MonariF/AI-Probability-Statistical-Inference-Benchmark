# INTENTIONALLY FLAWED CANDIDATE — evaluator practice only.
import numpy as np
from scipy.stats import binom

n, x, p0 = 40, 16, 0.25

# Error 1: CDF(x) is P(X <= x), not P(X >= x).
tail_probability = binom.cdf(x, n, p0)

# Error 2: this upper-tail probability is mislabeled as a two-sided p-value.
reported_p_value = binom.sf(x - 1, n, p0)

# Error 3: simulate under observed p-hat instead of null p0.
rng = np.random.default_rng()  # Error 4: no fixed seed.
draws = rng.binomial(n, x / n, size=10000)
mc_probability = np.mean(draws >= x)

# Error 5: Wald interval is mislabeled as exact.
p_hat = x / n
se = np.sqrt(p_hat * (1 - p_hat) / n)
claimed_exact_interval = (p_hat - 1.96 * se, p_hat + 1.96 * se)

print("Tail probability:", tail_probability)
print("Two-sided p-value:", reported_p_value)
print("Monte Carlo probability:", mc_probability)
print("95% exact confidence interval:", claimed_exact_interval)
