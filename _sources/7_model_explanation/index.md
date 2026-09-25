# 7. Model Explanation

A validated model tells you *that* it predicts. This chapter is about the separate, and surprisingly
treacherous, question of *how* — which features it uses, what it has learned, and what you are
entitled to say about the world on that basis.

The treachery starts earlier than people expect. It is not that black boxes are hard to interpret
and linear models are easy; it is that the obvious reading of a linear model's coefficients is
usually wrong, for reasons that apply to every predictive model ever fitted.

**In this chapter:**

- **[Explaining "Classical" Models](classical.ipynb)** — why coefficients are unstable, why a weight
  is not an importance, and the one transformation that makes a linear model's pattern interpretable.
- **[Black Boxes](black_box.ipynb)** — model-agnostic explanation, what it is good for, and the
  honest answer to whether an uninterpretable model can be trusted.
