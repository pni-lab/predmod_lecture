# 4. Fighting Overfitting: the Advent of Machine Learning

[Chapter 3](../3_cross_validation/index.md) taught us to *measure* predictive performance honestly,
and produced a picture to aim at: a valley, with oversimplification on one side and memorization on
the other. This chapter is about steering into it.

The tool is the **hyperparameter**, a setting that is not learned from the data during fitting but
chosen beforehand, and that controls how much freedom the model has. Adding such a dial to a linear
model is roughly what turns it into a machine learning model.

The last section of the chapter introduces the second way a predictive model can flatter itself,
which is harder to notice than overfitting and at least as common.

**In this chapter:**

- **[Reducing Complexity: a Brief Theory](theory_regularization.ipynb)**: feature selection, PCA,
  PLS, Ridge and LASSO, and why standardization is not optional.
- **[Reducing Complexity in Action](practice_regularization.ipynb)**: all five applied to the IXI
  data, and scikit-learn pipelines.
- **[Leakage](leakage.ipynb)**: how information about the test data reaches the model unnoticed, and
  what it does to the reported results.
