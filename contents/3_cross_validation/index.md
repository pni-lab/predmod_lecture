# 3. Honest Estimates of Predictive Performance

[Chapter 2](../2_linear_models/index.md) left us unable to trust the only number we had. The error
a model makes on the data it was fitted to can be driven to zero by adding predictors — real ones
or nonsense ones — so it says nothing about whether the model has learned anything.

This chapter fixes the measurement problem. It does not yet fix overfitting itself; that is
[chapter 4](../4_reducing_complexity/index.md). But nothing can be fixed before it can be measured.

**In this chapter:**

- **[Training and Test Sets](train_test.ipynb)** — evaluating on unseen data, and the complexity
  curve that the rest of the book is about.
- **[Cross-validation](cv.ipynb)** — getting an honest estimate without sacrificing a test set,
  what exactly that estimate refers to, and where it is still slightly wrong.
