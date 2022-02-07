# Theory 2.1: Linear Models

Linear models and alikes (e.g. ANOVA) are rudimental statistical tools in scientific analyses.
Probably you have also used them.

Besides their widespread applications, they provide a great starting point for 
understanding the predictive modelling, too.

Here we will briefly refresh your memories about the basics of linear models,
so that in the next section we can get them working in python and arrive at one of their limitations,
which provides a straightforward motivation for doing predictive modelling.

[Linear models](https://en.wikipedia.org/wiki/Linear_model) can be formalized as follows:

$$
Y_{i}=\beta _{0}+\beta _{1}\phi _{1}(X_{{i1}})+\cdots +\beta _{p}\phi _{p}(X_{{ip}})+\varepsilon _{i}\qquad i=1,\ldots ,n
$$
