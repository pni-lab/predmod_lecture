# 7. Model Explanation

A validated model tells us *that* it predicts. This chapter is about the separate, and surprisingly
treacherous, question of *how*: which features it uses, what it has learned, and what we are
entitled to say about the world on that basis.

The treachery starts earlier than most people expect. The familiar contrast between opaque black
boxes and readable linear models is misleading, because the obvious reading of a linear model's
coefficients is usually wrong too, for reasons that apply to every predictive model ever fitted.

**In this chapter:**

- **[Explaining "Classical" Models](classical.ipynb)**: why coefficients are unstable, why a weight
  is not an importance, and the one transformation that makes a linear model's pattern
  interpretable.
- **[Black Boxes](black_box.ipynb)**: model-agnostic explanation, what it can and cannot deliver,
  and under what conditions an uninterpretable model may still be trusted.
