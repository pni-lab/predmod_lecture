# Linear Models: a Brief Theory

## Linear Regression

Linear models and alikes (e.g. ANOVA) are rudimentary statistical tools in scientific analyses.
Probably you have also used them.

Beside their widespread applications, they provide a great starting point for 
understanding the predictive modelling, too.

Here we will briefly refresh your memories about the basics of linear models,
so that in the next section we can get them working in python and arrive at one of their limitations,
which provides a straightforward motivation for doing predictive modelling.

[Linear models](https://en.wikipedia.org/wiki/Linear_model) aim to deconstruct the dependent variable
(or target variable) $y = (y_1, \cdots, y_n)$ (consisting of n observations) into a sum of a constant $\beta _0$ (called the intercept) 
and the multiple of the predictor variable x, so that the difference between this sum and 
the target variable is minimal. 

$$
y_{i}=\beta _{0}+\beta _{1}x_{{i}}+\varepsilon _{i}
$$

The difference is usually denotes as $\varepsilon$ and
is subject to be minimized by dedicated algorithms
(e.g. [the method of least squares](https://en.wikipedia.org/wiki/Least_squares)).

$$
argmin_\beta \sum [ y_i - (\beta _{0}+\beta _{1}x_{{i}}) ]^2
$$


Todo: nice figure comes here

Linear regression models can trivially be extended
to handle multiple predictor variables (multiple linear regression):

$$
y_{i}=\beta _{0}+\beta _{1}(x_{{i1}})+\cdots +\beta _{p}x_{{ip}}+\varepsilon _{i}\qquad i=1,\ldots ,n
$$

Both the aim and the methods remain the same: we deconstruct
the target variable into a *weighted some* (i.e a [linear combination](https://en.wikipedia.org/wiki/Linear_combination))
of the predictors so that the result is as similar to the target variable as possible.

If we denote the matrix containing all predictors $\boldsymbol{$(x_1}, \cdots, \boldsymbol{x_n})$ as $X$ and the vector
$(b_0, \cdots, b_n)$ as $\boldsymbol{b}$ containing all beta coefficients then the quantity to be minimized is:

$$
argmin_\boldsymbol{b} \sum [ \boldsymbol{y} - \boldsymbol{b}X) ]^2
$$

```{note}
We will get back to this equation in section 4, when discussing the theoretical basis of regularized models,
the basics of machine learning.
```

Note that the higher the association between y and X is, the closer the linear model will
be able to match them and the smaller the error $\epsilon$ will be.
Therefore, fitting a linear model can be (and very commonly is) used to quantify the strength of the
association (correlation) between the target variable and the predictors with $R$, $R^2$, T- and p-values.

```{note}
Linear regression models can be easly extended to deal with factor variables,
to reproduce ANOVA and related tests. Linear models can be also extended to handle
a binary or factorial target variable (logistic or multinomial regression).
```

## Predictions

After fitting a linear model, we can obtain "predictions" $\hat{y}$ for an arbitrary values of X:

$$
\hat{y} = \boldsymbol{b}X
$$

In the next page, we will see how one can perform linear regression in python.


