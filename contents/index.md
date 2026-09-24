```{image} cover.png
:alt: Book cover: A Gentle Introduction to Predictive Modelling
:width: 80%
:align: left
```

```{note}
*Cover created in 2021 by text2art AI, seeded with the book title. It is a memento of the state-of-the-art of artificial intelligence in 2021, and an artifact of the accelerating development of AI.*
```

# A Gentle Introduction to Predictive Modelling

This is an interactive book about predicting things — specifically, about predicting them
*honestly*. It is written for researchers who are comfortable with statistical inference and
suspicious of machine learning, and it argues that the distance between the two is much shorter
than it looks.

Every concept is developed through a single running example — estimating a person's age from the
structure of their cortex — with code you can run, modify and break. No neuroimaging background is
assumed.

```{admonition} Start here
:class: tip
New to the book? Read the [introduction](introduction.md), then work through the chapters in order:
they build on one another, and the later ones repeatedly undo conclusions the earlier ones invited
you to draw. [Chapter 1](1_python_basics/index.md) sets up the python and the dataset; if you
already write python, skim it and start at chapter 2.
```

**The argument, step by step:**

1. The error a model makes on the data it was fitted to tells you very little — and for a
   sufficiently complex model, next to nothing
   ([chapter 2](2_linear_models/index.md)).
2. Measuring it on unseen data tells you a great deal
   ([chapter 3](3_cross_validation/index.md)).
3. Controlling model complexity is what makes prediction work — and is where machine learning
   begins ([chapter 4](4_reducing_complexity/index.md)).
4. Every choice you make by looking at your results has to be paid for
   ([chapter 5](5_hyperparameter_optimization/index.md)).
5. An honest performance estimate still does not tell you whether the model travels to another
   site, whether it measures what you meant, or who it fails
   ([chapter 6](6_validity/index.md)).
6. Reading a model — even a linear one — is harder than it looks, and the obvious reading is
   usually wrong ([chapter 7](7_model_explanation/index.md)).
7. Fancier algorithms buy less than you would expect, and only once you have the data to feed them
   ([chapter 8](8_complex_models/index.md)).
8. Three studies showing what all of this looks like in practice — done thoroughly, done honestly,
   and done well but on the wrong question ([chapter 9](9_examples/index.md)).

All practice pages are live notebooks: click the rocket at the top of any page to run them in your
browser, in Binder or in Colab.

This book is under active development. Corrections, suggestions and questions are welcome as
[issues](https://github.com/pni-lab/predmod_lecture/issues/new).
