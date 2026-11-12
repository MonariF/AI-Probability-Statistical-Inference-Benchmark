import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from reference_solution import analyse_binomial, monte_carlo_upper_tail


def test_upper_tail_probability_is_valid():
    r = analyse_binomial()
    assert 0.0 < r["upper_tail_probability"] < 1.0


def test_exact_test_and_interval_are_valid():
    r = analyse_binomial()
    assert 0.0 <= r["two_sided_p_value"] <= 1.0
    assert 0.0 < r["ci_lower"] < r["ci_upper"] < 1.0


def test_monte_carlo_is_reproducible():
    assert monte_carlo_upper_tail(seed=12345, simulations=50000) == monte_carlo_upper_tail(seed=12345, simulations=50000)


def test_monte_carlo_approximates_analytical_tail():
    r = analyse_binomial()
    tolerance = 5 * r["mc_standard_error"] + 0.002
    assert abs(r["mc_estimate"] - r["upper_tail_probability"]) < tolerance


def test_decision_matches_p_value():
    r = analyse_binomial()
    assert r["reject_null"] == (r["two_sided_p_value"] < 0.05)
