# 9. Scientific Examples

Three studies, chosen because each one teaches something the other two cannot.

They are not here as illustrations of technique — the technique is in chapters 2 to 8. They are here
because predictive modelling is ultimately a craft of judgement, and judgement is learned from cases:
what a thorough validation programme actually looks like when someone carries it out over a decade,
what happens to a good cross-validated result when it meets independent data, and how a model can
satisfy every methodological requirement in this book and still be the wrong model.

**In this chapter:**

- **[The Neurologic Pain Signature](pain_signature.md)** — a brain-based measure of pain intensity,
  validated across scanners, populations and a pharmacological manipulation, and progressively
  deflated by a decade of people testing what it really measures. The lesson: **specificity is only
  ever relative to the alternatives you tested against.**
- **[A Pre-registered Model, and the Price of Honesty](registered_model.md)** — a study that reports
  both its cross-validated and its externally validated performance, and the five-fold gap between
  them. The lesson: **nested cross-validation does not buy generalizability.**
- **[The Model That Was Accurate and Wrong](wrong_target.md)** — a health-care algorithm, externally
  validated on 3.7 million patients, well calibrated, not using race as a feature, and racially
  discriminatory in effect. The lesson: **no methodological rigour can detect the wrong target.**

Read in that order, they trace the argument of the book past its own end. Chapters 3 to 5 teach you
to measure performance honestly. Chapter 6 teaches you that honest performance is not the same as a
valid model. These three studies show what that distinction costs, and what it looks like when
people take it seriously.
