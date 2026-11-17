# 8. Complex Models: from Ensembles to Deep Learning

This book has deliberately used a single model throughout (a linear regression with a penalty on its
coefficients), because every concept that matters is visible in it, and visible more clearly for the
absence of machinery.

The toolbox is of course much larger, and this chapter surveys it: bagging, random forests,
boosting, kernel methods and neural networks. The organizing question here is what each algorithm
*assumes*, and therefore when its assumptions are likely to suit a given problem, rather than which
one wins in general.

The chapter then runs all of them on the book's data, tuned fairly by nested cross-validation, and
reports what the extra complexity actually buys. The benefit is probably smaller than expected, and
it depends strongly on how much data is available.

**In this chapter:**

- **[From Ensembles to Deep Learning](ensembles.ipynb)**: inductive bias, the ensemble methods, when
  deep learning helps, and a head-to-head comparison on the IXI data.
