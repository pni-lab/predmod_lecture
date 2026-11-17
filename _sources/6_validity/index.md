# 6. Generalizability, Validity, Fairness

[Chapter 5](../5_hyperparameter_optimization/index.md) ended with a complete recipe for building a
model and reporting its performance honestly. This chapter is about the questions that recipe leaves
open.

An honest performance estimate tells us how well a model predicts new participants *drawn like the
ones we have*. It cannot tell us whether the model works at another hospital, whether it has learned
the thing we believe it has learned, or for whom it works badly. These three questions are the
subject of the three pages here. A model that has survived this far is typically threatened
less by overfitting or leakage than by the tacit assumption that the world will go on resembling the
training set.

**In this chapter:**

- **[Generalizability](generalizability.ipynb)**: internal versus external validation, the three
  ways a distribution can shift, and what a five-fold drop in explained variance between
  cross-validated and externally validated performance looks like in practice.
- **[Validity and Specificity](validity.ipynb)**: whether the model measures the construct we
  intended, why the obvious confounder check is close to worthless, and how to test for confounding
  properly with `mlconfound`.
- **[Fairness](fairness.ipynb)**: which subgroups the model serves poorly, and the failure mode that
  no amount of methodological rigour can detect, namely the choice of the wrong prediction target.
