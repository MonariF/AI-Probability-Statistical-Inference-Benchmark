# AI Evaluation Benchmark: Probability, Statistical Inference and Mathematical Reasoning

**Author:** Dr. Fred Nyamitago Monari, PhD  
**Specialization:** Applied Statistics | Probability | Statistical Inference | Computational Statistics

## 1. Project Overview

This independent portfolio project demonstrates the design, implementation and evaluation of computational tasks in probability and statistical inference using Python, NumPy and SciPy.

The benchmark evaluates whether a candidate can correctly calculate probability distributions, conduct exact hypothesis tests, construct confidence intervals and validate Monte Carlo simulations against analytical results.

**Transparency Statement:** This is a self-directed academic portfolio project. It demonstrates relevant mathematical, statistical and computational evaluation skills. It is not evidence of previous paid AI-training or commercial AI-model evaluation employment.

## 2. Benchmark Problem

A process has a claimed success probability of 0.25. In 40 independent trials, 16 successes are observed.

We investigate:

\[
X\sim \operatorname{Binomial}(40,0.25)
\]

The benchmark requires:

- Calculation of the upper-tail probability \(P(X\geq16)\).
- An exact two-sided binomial hypothesis test.
- A 95% Clopper-Pearson confidence interval.
- Monte Carlo estimation using 300,000 simulations.
- Comparison of analytical and simulation-based results.

## 3. Technical Competencies

- Probability theory and binomial distributions.
- Exact statistical hypothesis testing.
- Confidence interval estimation.
- Monte Carlo simulation.
- Statistical reasoning and interpretation.
- Reproducible scientific computing.
- Identification of errors in AI-generated statistical solutions.
- Objective technical evaluation and grading.

## 4. Repository Structure

```text
AI-Probability-Statistical-Inference-Benchmark/
├── README.md
├── requirements.txt
├── task/
│   └── benchmark_task.md
├── src/
│   ├── reference_solution.py
│   └── flawed_candidate.py
├── evaluation/
│   ├── rubric.md
│   └── evaluator_notes.md
└── tests/
    └── test_reference_solution.py
```

## 5. Installation and Reproducibility

**Requirements:** Python 3.10 or later.

### Clone the repository

```bash
git clone https://github.com/MonariF/AI-Probability-Statistical-Inference-Benchmark.git
cd AI-Probability-Statistical-Inference-Benchmark
```

### Create a virtual environment

```bash
python -m venv .venv
```

Windows activation:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the reference solution

```bash
python src/reference_solution.py
```

### Run automated tests

```bash
python -m pytest -q
```

## 6. Evaluation Framework

The benchmark uses a 100-point scoring rubric covering:

| Criterion | Weight |
|---|---:|
| Probability model and notation | 10 |
| Analytical upper-tail probability | 15 |
| Exact hypothesis testing | 15 |
| Exact confidence interval | 15 |
| Monte Carlo simulation | 15 |
| Numerical validation | 10 |
| Statistical interpretation | 10 |
| Reproducibility and communication | 10 |
| **Total** | **100** |

Critical errors include incorrect discrete probability tails, confusing one-sided probabilities with two-sided p-values, simulating under the wrong null probability and misidentifying confidence interval methods.

## 7. Technical Tools

- Python
- NumPy
- SciPy
- pytest

## 8. Research and Professional Background

Dr. Fred Nyamitago Monari is a Computational Mathematician and Applied Statistician holding a PhD in Applied Statistics.

He is a Lecturer and Research Fellow at Kisii University, Kenya. His research interests include computational statistics, mathematical modelling, machine learning, statistical inference and AI-enabled scientific research.

He has authored and co-authored more than 20 research publications.

## 9. Limitations and Future Development

This is a compact educational benchmark based on independent Bernoulli trials with a common success probability.

Future extensions include Bayesian inference, statistical power calculations, likelihood methods, multiple testing and simulation-based calibration.

---

**GitHub Portfolio:** https://github.com/MonariF

**Google Scholar:** https://scholar.google.com/citations?user=oJe6jTkd67MC

**Contact:** fnyamitago@gmail.com

*This project is an independent technical demonstration, not a validated production benchmark or evidence of paid AI-training employment.*
