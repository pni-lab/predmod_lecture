# Feature Reduction: brief theory

Reducing the number of features naturally reduces model complexity.
In the next section we will see some of the most common strategies to do so.

This section provides some theoretical background that will be useful in the next section.

## Selecting best features based on their association with the target

A possible way of reducing the complexity of a model
is to simply retain those feature only, which seem to be correlated to the target in
the training set.

This can be done based on any conventional statistical inference method.
We can for example take (the absolute value of)
the Pearson's correlation coefficient:

$$
r = \frac{{}\sum_{i=1}^{n} (x_i - \overline{x})(y_i - \overline{y})}
{\sqrt{\sum_{i=1}^{n} (x_i - \overline{x})^2(y_i - \overline{y})^2}}
$$

In theory an arbitrary threshold can be drawn for the test statistic and
can be considered as a hyperparamter.
Changing it will change model complexity.

Higher thresholds -> less parameters -> lower complexity
Lower thershold -> more predictors -> higher complexity

In case of highly collinear (correlated) features, this approach may not be efficient in reducing
complexity, as it may retain too many features.

## Principal Component Analysis

A somewhat more sophisticated approach is to apply dimensionality reduction,
for instance principal component analysis (PCA).

As defined in [Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis): PCA is defined as an orthogonal linear transformation that transforms
the data to a new coordinate system such that the greatest variance
by some scalar projection of the data comes to lie on the first coordinate
(called the first principal component),
the second-greatest variance on the second coordinate, and so on.

Loosely speaking, in case of correlated (collinear) features, PCA decomposes
the common component of the features into one single variable. PCA components will, therefore,
be orthogonal to each other.

Retaining the first k principal component will therefore ensure that as much
total variance is reatined from all features as possible and allows for low-complexity
models even in case of highly collinear features.

:::{figure-md} pca
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/GaussianScatterPCA.svg/1024px-GaussianScatterPCA.svg.png" alt="fishy" width="400px">

Principal Component Analysis in two dimensions (Source: [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/GaussianScatterPCA.svg/1024px-GaussianScatterPCA.svg.png

), author: Nicoguaro, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))*.
:::

# Partial Least Squares

As compared to selecting the K best features and PCA,
[Partial Least Squares](https://en.wikipedia.org/wiki/Partial_least_squares_regression) (PLS) brings the best of both words.

Instead of finding hyperplanes of maximum variance between the response
and independent variables (as PCA does),
PLS finds a linear regression model by projecting the predicted
variables and the observable variables to a new space. 

The order of PLS components does not simply reflect how much total variance they explain.
It reflects, how much variance they explain in the target variable.

PLS often achieves a comparable performance to PCA, but with fewer components included. 

:::{note}
Importantly, PLS can be applied to predict multiple variables at the same time.
:::




