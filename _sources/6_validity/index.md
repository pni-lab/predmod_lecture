# 6. Generalizability, Validity, Fairness

[Chapter 5](../5_hyperparameter_optimization/index.md) ended with a complete recipe for building a
model and reporting its performance honestly. Everything in this chapter is about the questions that
recipe cannot answer.

An honest performance estimate tells you how well your model predicts new participants *drawn like
yours*. It does not tell you whether the model works at another hospital, whether it learned the
thing you think it learned, or whom it works badly for. Those three questions are the subject of the
three pages here — and the first villain of a model that has survived this far is no longer
overfitting or leakage, but the quiet assumption that the world will keep looking like your
training set.

**In this chapter:**

- **[Generalizability](generalizability.ipynb)** — internal versus external validation, the three
  ways a distribution can shift, and what a five-fold gap between cross-validated and externally
  validated performance looks like in practice.
- **[Validity and Specificity](validity.ipynb)** — whether the model measures the construct you
  meant, why the obvious confounder check is worthless, and how to test for confounding properly
  with `mlconfound`.
- **[Fairness](fairness.ipynb)** — who the model works for, and the failure mode that no amount of
  methodological rigour can detect: choosing the wrong thing to predict.
