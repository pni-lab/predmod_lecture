# A Pre-registered Model, and the Price of Honesty

**What it shows: what happens to a cross-validated result when it meets independent data.**

Every method in this book was designed to stop you fooling yourself. The obvious question is whether
they work. Answering it requires a study that reports *both* the cross-validated performance and the
externally validated performance of the same model — and almost nobody does, because the first number
is usually the one in the abstract.

{cite:t}`kincses2024rcpl` is that study.

## The question and the design

Can a five-minute resting-state scan — the participant lies still and does nothing — predict how
strongly that person learns from pain? Pain acts as a teaching signal, and altered pain-related
learning is a feature of chronic pain, so an accessible marker of it would be useful. The prediction
target was a differential conditioning score: how much the unpleasantness rating of a pain-predicting
cue changed relative to a safety cue.

The modelling is the recipe from [chapter 5](../5_hyperparameter_optimization/index.md):
partial-correlation connectivity between 122 regions, univariate feature selection followed by ridge
regression, assembled as a pipeline so that selection happens inside the loop, with the number of
features and the regularization strength tuned in an **inner** cross-validation and performance
estimated in an **outer** one.

Then it goes one step further, in a way this book has recommended but not yet seen done. The final
model — ten connections, a fixed $\alpha$, and every preprocessing parameter — was **frozen and
publicly pre-registered** before the validation data were analyzed. The authors call this a
*registered model* design. Two independent cohorts followed, one of them deliberately dissimilar:
different personnel, different paradigm, and a different pain modality (visceral rather than heat).

## The result

| | correlation | variance explained |
|---|---|---|
| discovery sample (n = 25), nested cross-validation | **r = 0.72** | ~52% |
| external validation (n = 49, two cohorts) | **r = 0.34** | **8–12%** |

Roughly five-sixths of the explained variance did not survive.

It is worth being precise about what did *not* go wrong here, because the list is long. There was no
leakage: feature selection and tuning were inside the loops. There was no hyperparameter fishing: the
model was registered before validation. There was no publication sleight of hand: the abstract leads
with the 8–12%, not with the 52%. The senior author is the same person who wrote the confounder-testing
tool of [chapter 6](../6_validity/validity.ipynb), and the paper duly reports that age, four separate
measures of head motion, depression and several pain-related questionnaires showed no evidence of
biasing the model.

The authors' own explanation is the one this book has been building towards. Cross-validation in a
small sample is **unbiased but highly variable**: right on average across many hypothetical studies,
and capable of landing far above the truth in any single one. With n = 25, far above. Papers are
written about the studies that landed high.

## What to take from it

**Nested cross-validation does not buy you generalizability.** It buys you an estimate that is not
inflated by leakage or by tuning. Those are different things, and this study separates them cleanly:
everything internal was done correctly, and the external number was still a third of the internal one.

**Small samples produce variable estimates, and variability is selected on.** This is the mechanism
behind much of the replication difficulty in brain-behaviour prediction {cite:p}`spisak2023multivariate`.
No individual study need be dishonest for the literature as a whole to be over-optimistic.

**Register the model.** A frozen, publicly posted specification makes an entire class of errors
arithmetically impossible rather than merely unlikely, and costs nothing but nerve.

**Report the honest number even when it is smaller.** An external r of 0.34 for predicting an
individual difference from resting-state connectivity is a respectable result, and a great deal more
useful than an r of 0.72 that nobody can reproduce.

## A note on comparing across studies

The [pain signature](pain_signature.md) reports near-ceiling accuracies; this study reports r = 0.34.
That comparison is meaningless, and it is worth saying why, because the same mistake is made
constantly.

The signature is a **within-person, task-evoked state** measure: given two scans from one person,
which one hurt more? Individual differences are removed by design, and the effect sizes are
correspondingly large. This model makes a **between-person, task-free trait** prediction: given a
resting scan, what kind of learner is this person? That is intrinsically harder, and the achievable
ceiling is much lower — as {cite:t}`han2022effect` demonstrated for the pain signature itself, whose
own between-person performance is weak.

Different estimands, different ceilings. Before comparing two models' numbers, check that they were
answering the same question.

## Sources

- {cite:t}`kincses2024rcpl` — the study, with open code, open data, and the pre-registration.
- {cite:t}`spisak2023multivariate` — sample size and replicability in multivariate brain-behaviour
  prediction.
- {cite:t}`spisak2022confounding` — the confounder tests used in the paper.
