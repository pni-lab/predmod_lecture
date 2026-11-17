# 5. Hyperparameter Optimization and Nested Cross-validation

[Chapter 4](../4_reducing_complexity/index.md) gave us dials to control model complexity, and then
showed that turning them while watching cross-validated performance quietly inflates the result.

This chapter closes the loop. In both cases the remedy is the same: a decision that must not be
influenced by the data the model will be judged on has to be made inside a cross-validation of its
own.

By the end of the chapter we have a complete and honest recipe for building a predictive model and
reporting what it does.

**In this chapter:**

- **[Cross-validation Revisited](cross_validation_revisited.ipynb)**: feature selection inside the
  loop, and pipelines as leakage prevention by construction.
- **[Nested Cross-validation](nested_cross_validation.ipynb)**: training, validation and test sets,
  `GridSearchCV`, how much the nesting actually changes, and the recipe itself.
