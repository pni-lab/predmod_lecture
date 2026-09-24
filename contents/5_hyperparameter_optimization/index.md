# 5. Hyperparameter Optimization and Nested Cross-Validation

[Chapter 4](../4_reducing_complexity/index.md) gave us dials to control model complexity, and then
showed that turning them by looking at cross-validated performance quietly inflates the result.

This chapter closes the loop. The answer, both times, is the same move: if a decision must not be
influenced by the data you will be judged on, make that decision inside a cross-validation of its
own.

By the end of it you will have a complete, honest recipe for building and reporting a predictive
model.

**In this chapter:**

- **[Cross-validation Revisited](cross_validation_revisited.ipynb)** — feature selection inside the
  loop, and pipelines as leakage prevention by construction.
- **[Nested Cross-validation](nested_cross_validation.ipynb)** — training, validation and test sets;
  `GridSearchCV`; how much the nesting actually changes; and the recipe.
