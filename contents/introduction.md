# Introduction

```{image} img.png
:alt: Illustration of brains and data
:class: bg-primary mb-1
:width: 100%
:align: left
```

Predictive modelling and machine learning have become central to biomedical research, and they hold
real promise for delivering biomarkers that change clinical practice and public health
{cite:p}`vogt2018machine, kent2018personalized, spisak2020pain, walsh2021dome`.

For many researchers, though, "machine learning" remains a slightly mysterious term — more familiar
from science fiction than from their own work. This is odd, because the same researchers routinely
use mixed-effects models, navigate complicated analysis pipelines, and think carefully about
confounding. The obstacle is not mathematical sophistication. It is that predictive modelling asks a
different question from the one their training prepared them for.

## Who this book is for

You, if you are comfortable fitting a linear model and interpreting a p-value, and would like to
know what changes when the goal becomes prediction rather than inference.

The aim of this book is to demystify predictive modelling by showing that its simplest — and
already very powerful — forms are as accessible as the tools you use every day. Not by
simplifying the ideas, but by being concrete about them.

## How it works

Everything is illustrated on one dataset, with python code, in a single running example: predicting
age from brain structure. The data is structural MRI, but no neuroimaging knowledge is assumed. If
you would like some background anyway, there are
[many](https://carpentries-incubator.github.io/SDC-BIDS-sMRI/aio/index.html) good
[resources](https://andysbrainbook.readthedocs.io/en/latest/) available free online.

Practice pages are interactive notebooks. They run on your own machine or, with one click, in the
cloud — look for the rocket icon at the top of the page. Exercises throughout ask you to modify the
code, and each has a worked solution folded underneath it. Open the solution *after* you have tried;
the failures are where the learning is.

```{tip}
The single best way to use this book is to work through it with **your own dataset** alongside the
example. It is harder, and it is the difference between recognising these concepts and owning them.
```

## What to expect

The book has a plot, and it is not a flattering one. Chapter by chapter, results that look
impressive turn out to be artefacts, and the methods that fix them introduce subtler problems of
their own. Two villains recur: **overfitting**, which makes models look good on the data they were
built from, and **leakage**, which makes them look good even on data they were not.

This is not pessimism. The point is that predictive modelling comes with a small number of specific
failure modes, that they are well understood, and that avoiding them is mostly a matter of
discipline rather than mathematics. By [chapter 5](5_hyperparameter_optimization/index.md) you will
have a complete recipe for building a model and reporting its performance honestly.

The book focuses on simple, explainable models. But it also shows how the predictive framework lets
you use a genuine "black box" without giving up confidence in what it does — because in this
framework, trust comes from how a model was *validated*, not from whether you can read its
coefficients.

## A living document

This is not a conventional textbook. It is a Jupyter Book under continuous development. If something
is wrong, unclear, or missing, please open an
[issue](https://github.com/pni-lab/predmod_lecture/issues/new) — that is how it gets better.

[![GitHub issues](https://img.shields.io/github/issues/pni-lab/predmod_lecture.svg)](https://github.com/pni-lab/predmod_lecture/issues/)

Have fun discovering a new way of dealing with your data.
