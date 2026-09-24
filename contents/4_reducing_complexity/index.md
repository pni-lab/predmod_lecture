# 4. Fighting Overfitting: the Advent of Machine Learning

[Chapter 3](../3_cross_validation/index.md) taught us to *measure* predictive performance honestly,
and produced a picture to aim at: a valley, with oversimplification on one side and memorisation on
the other. This chapter is about steering into it.

The tool is the **hyperparameter**: a setting that is not learned from the data during fitting, but
chosen beforehand, and that controls how much freedom the model has. Adding such a dial to a linear
model is, in essence, what turns it into a machine learning model.

And then, in the last section, the second villain arrives.

**In this chapter:**

- **[Reducing Complexity: a Brief Theory](theory_regularization.ipynb)** — feature selection, PCA,
  PLS, Ridge and LASSO, and why standardisation is not optional.
- **[Reducing Complexity in Action](practice_regularization.ipynb)** — all five applied to the IXI
  data, and scikit-learn pipelines.
- **[The Second Villain: Leakage](leakage.ipynb)** — how information about the test data reaches
  your model without you noticing, and what it does to your results.
