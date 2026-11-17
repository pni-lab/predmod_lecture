# 3. Honest Estimates of Predictive Performance

[Chapter 2](../2_linear_models/index.md) left us unable to trust the only number we had. The error a
model makes on the data it was fitted to can be driven all the way to zero by adding predictors
(real ones or nonsense ones alike), so on its own it says nothing about whether the model has
learned anything.

This chapter fixes the measurement problem, though not yet overfitting itself, which is the subject
of [chapter 4](../4_reducing_complexity/index.md). Measurement comes first, since a problem that
cannot be quantified cannot be addressed.

**In this chapter:**

- **[Training and Test Sets](train_test.ipynb)**: evaluating on unseen data, and the complexity
  curve that the rest of the book is about.
- **[Cross-validation](cv.ipynb)**: obtaining an honest estimate without sacrificing a test set,
  what exactly that estimate refers to, and in which direction it is still slightly off.
