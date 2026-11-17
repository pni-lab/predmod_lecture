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

For many researchers, though, "machine learning" remains a slightly mysterious term, more familiar
from science fiction than from their own work. This is somewhat odd, given that the same researchers
routinely use mixed-effects models, navigate complicated analysis pipelines, and think carefully
about confounding. The obstacle is rarely mathematical sophistication, but rather that predictive
modelling asks a different question from the one their training prepared them for.

## Who this book is for

You, if you are comfortable fitting a linear model and interpreting a p-value, and would like to
know what changes when the goal becomes prediction rather than inference.

The aim of the book is to demystify predictive modelling by showing that its simplest (and already
very powerful) forms are as accessible as the tools you use every day, by being concrete about the
ideas rather than by simplifying them.

## How it works

Everything is illustrated on one dataset, with python code, in a single running example: predicting
age from brain structure. The data is structural MRI, but no neuroimaging knowledge is assumed. If
you would like some background anyway, there are
[many](https://carpentries-incubator.github.io/SDC-BIDS-sMRI/aio/index.html) good
[resources](https://andysbrainbook.readthedocs.io/en/latest/) available free online.

Practice pages are interactive notebooks. They run on your own machine or, with one click, in the
cloud (look for the rocket icon at the top of the page). Exercises throughout ask you to modify the
code, and each has a worked solution folded underneath it. Open the solution *after* you have tried,
since most of the learning happens in the failures.

```{tip}
The single best way to use this book is to work through it with **your own dataset** alongside the
example. It is harder, and it is the difference between recognizing these concepts and owning them.
```

## What to expect

The chapters follow a storyline that is not especially flattering to the field: results that look
impressive turn out to be artefacts, and the methods that fix them introduce subtler problems of
their own. Two failure modes recur throughout, namely **overfitting**, which makes models look good
on the data they were built from, and **leakage**, which makes them look good even on data they were
not.

The intention is reassurance rather than pessimism. Predictive modelling comes with a small number of
specific failure modes, they are reasonably well understood, and avoiding them is mostly a matter of
discipline rather than of mathematics. By [chapter 5](5_hyperparameter_optimization/index.md) you
will have a complete recipe for building a model and reporting its performance honestly.

The book focuses on simple, explainable models. It also shows, however, how the predictive framework
lets you use a genuine "black box" without giving up confidence in what it does, since trust here
comes from the way a model was *validated*.

## A living document

This is a Jupyter Book under continuous development rather than a conventional textbook. If
something is wrong, unclear, or missing, please open an
[issue](https://github.com/pni-lab/predmod_lecture/issues/new).

[![GitHub issues](https://img.shields.io/github/issues/pni-lab/predmod_lecture.svg)](https://github.com/pni-lab/predmod_lecture/issues/)

Have fun discovering a new way of dealing with your data.
