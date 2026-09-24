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
you to draw.
```

**The argument, in four steps:**

1. A model's error on the data it was fitted to tells you nothing
   ([chapter 2](2_linear_models/index.md)).
2. Measuring it on unseen data tells you a great deal
   ([chapter 3](3_cross_validation/index.md)).
3. Controlling model complexity is what makes prediction work — and is where machine learning
   begins ([chapter 4](4_reducing_complexity/index.md)).
4. Every choice you make by looking at your results has to be paid for
   ([chapter 5](5_hyperparameter_optimization/index.md)).

All practice pages are live notebooks: click the rocket at the top of any page to run them in your
browser, in Binder or in Colab.

This book is under active development. Corrections, suggestions and questions are welcome as
[issues](https://github.com/pni-lab/predmod_lecture/issues/new).
