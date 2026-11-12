import numpy as np
from scipy.stats import binom, binomtest

N, X_OBSERVED, P_NULL = 40, 16, 0.25
ALPHA, SIMULATIONS, SEED = 0.05, 300_000, 2026


def monte_carlo_upper_tail(n=N, p=P_NULL, observed=X_OBSERVED,
                           simulations=SIMULATIONS, seed=SEED):
    if n <= 0 or simulations <= 0:
        raise ValueError("n and simulations must be positive.")
    if not 0 <= p <= 1 or not 0 <= observed <= n:
        raise ValueError("Invalid probability or observed count.")
    rng = np.random.default_rng(seed)
    draws = rng.binomial(n=n, p=p, size=simulations)
    estimate = float(np.mean(draws >= observed))
    se = float(np.sqrt(estimate * (1.0 - estimate) / simulations))
    return estimate, se


def analyse_binomial():
    upper = float(binom.sf(X_OBSERVED - 1, N, P_NULL))
    test = binomtest(X_OBSERVED, n=N, p=P_NULL, alternative="two-sided")
    ci = test.proportion_ci(confidence_level=1.0 - ALPHA, method="exact")
    mc, mc_se = monte_carlo_upper_tail()
    return {
        "observed_proportion": X_OBSERVED / N,
        "upper_tail_probability": upper,
        "two_sided_p_value": float(test.pvalue),
        "ci_lower": float(ci.low), "ci_upper": float(ci.high),
        "mc_estimate": mc, "mc_standard_error": mc_se,
        "simulations": SIMULATIONS, "seed": SEED,
        "reject_null": bool(test.pvalue < ALPHA),
    }


def main():
    r = analyse_binomial()
    print("Binomial probability and exact inference benchmark")
    print(f"n={N}, observed successes={X_OBSERVED}, null p={P_NULL}")
    print(f"Observed proportion: {r['observed_proportion']:.4f}")
    print(f"Analytical P(X >= {X_OBSERVED}): {r['upper_tail_probability']:.8f}")
    print(f"Two-sided exact p-value: {r['two_sided_p_value']:.8f}")
    print(f"95% Clopper-Pearson CI: ({r['ci_lower']:.6f}, {r['ci_upper']:.6f})")
    print(f"Monte Carlo estimate: {r['mc_estimate']:.8f}")
    print(f"Monte Carlo standard error: {r['mc_standard_error']:.8f}")
    print(f"Replicates: {r['simulations']}; seed: {r['seed']}")
    print("Decision at alpha=0.05:", "Reject H0" if r["reject_null"] else "Do not reject H0")
    print("Upper-tail probability and two-sided p-value are different quantities.")


if __name__ == "__main__":
    main()
