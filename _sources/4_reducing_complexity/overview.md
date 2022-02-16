# Overview

In the previous sections, we have seen that
the more complex a model is (and the less data we have), the more it will be prone to overfitting.

We have also seen that models that severely overfit the training sample, will not generalize well
to unseen data.

Finding the "sweat spot" in terms of model complexity lies in the heart of
predictive modelling. True machine learning models facilitates finding this sweat spot
with so-called hyperparamters that allow fine-tuning
different aspects of model complexity.

There are two basic methods to reduce model complexity:
- reducing the *number* of internal free parameters
that are optimised during model fitting. This is discussed in the [next two sections](theory_feature_reduction.md)
- introducing a *penalty* for complex models during model fitting,
  that prefers if the model leaves many of its parameters unused (zero coefficient).
  This process is called regularization and is discussed at the
  [end of this](theory_regularization.md) chapter.
