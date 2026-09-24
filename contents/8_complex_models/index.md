# 8. Complex Models: from Ensembles to Deep Learning

This book has deliberately used one model throughout — a linear regression with a penalty on its
coefficients — because every concept that matters is visible in it, and visible more clearly for the
absence of machinery.

The toolbox is much larger, and this chapter surveys it: bagging, random forests, boosting, kernel
methods and neural networks. The organising question is not which algorithm wins, but what each one
*assumes*, and therefore when its assumptions are likely to suit your problem.

The chapter also does something the literature rarely does: it runs all of them on the book's data,
tuned fairly by nested cross-validation, and reports what the extra complexity actually buys. The
answer is smaller than you might expect, and it depends on how much data you have.

**In this chapter:**

- **[From Ensembles to Deep Learning](ensembles.ipynb)** — inductive bias, the ensemble methods, when
  deep learning helps, and an honest head-to-head comparison on the IXI data.
