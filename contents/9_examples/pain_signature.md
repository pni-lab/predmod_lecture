# The Neurologic Pain Signature

**What it shows: how far a predictive model can be pushed, and where specificity ends.**

Pain is measured by asking. That is not a failure of imagination — self-report is the appropriate
standard for a subjective experience — but it leaves obvious gaps: patients who cannot report,
disputes about whether reported pain is "real", and no way to separate the components of a pain
experience. Two decades of fMRI research had produced a well-known set of regions that activate
during pain, collectively the "pain matrix", but nothing that could put a number on an individual's
pain.

{cite:t}`wager2013fmri` asked the predictive question instead.

## What they did

The target was reported pain intensity from noxious heat; the features were whole-brain voxel-wise
activity; the model was LASSO-PCR — principal components of the voxel data, followed by an
L1-penalized regression, with the coefficients mapped back into voxel space. The result is a single
whole-brain **weight map**, and applying it to a new brain image is a dot product.

The validation is the part worth studying, because the paper walks the entire ladder of
[chapters 3 to 6](../3_cross_validation/index.md) in one publication:

| step | what they did |
|---|---|
| cross-validation | leave-one-**subject**-out on 20 participants — the correct unit, since trials within a person are not independent |
| independent test sample | 33 new participants, **a different scanner** (3T Philips rather than 1.5T GE), weights frozen |
| new population and paradigm | 40 participants in an emotionally loaded task |
| discriminant validity | the signature tested against things it should *not* respond to |
| causal manipulation | remifentanil, an opioid, in an open/hidden infusion design |

Sensitivity and specificity were 93–95% for distinguishing painful from non-painful heat in both the
training study and the independent sample, and 100% and 99% for distinguishing pain from
*anticipating* pain. The opioid reduced the signature response by 53%, with **no difference between
open and hidden infusion**, which separates the drug's pharmacology from the patient's expectation
of relief.

## Why this belongs in this book

**The weights were published.** That is what turned a paper into a research programme: any lab can
apply the frozen map to its own data, and many have — including adversarially. Contrast this with the
usual situation, where a model exists only as a number in an abstract.

**They went looking for the ways it could be wrong.** In the original paper, participants who had
recently been through an unwanted breakup viewed photographs of the ex-partner. The signature
distinguished physical pain from that experience well — and could not distinguish the ex-partner from
a friend at better than chance, which is exactly what it should not be able to do. Later work showed
that patterns trained on physical pain and on social rejection are essentially uncorrelated and each
performs at chance on the other's task, even within the regions claimed to represent both
{cite:p}`woo2014separate`. The signature does not track observed pain in someone else
{cite:p}`krishnan2016somatic`, nor picture-induced negative affect {cite:p}`chang2015sensitive`.

**The follow-up literature deflated the overreading, and the original authors led it.** The 2013
paper was widely read as delivering an objective pain-o-meter. {cite:t}`han2022effect` assembled ten
studies and separated two effects that the original design conflated: *within-person* prediction
(does this trial hurt more than that one, in the same person) is very strong, with a mean effect size
of 1.45 across eight studies; *between-person* prediction (does this person report more pain than
that one) is weak and was significant in only one study out of eight. The signature is a within-person
mechanistic measure, not a between-person diagnostic. {cite:t}`zunhammer2018placebo` pooled 20
studies and found that placebo reduced reported pain roughly eight times more than it reduced the
signature — so a large part of what makes pain better is invisible to it. And as a standalone
diagnostic for chronic pain it performs poorly: 68% accuracy for fibromyalgia, where a combination of
patterns reached 93% {cite:p}`lopezsola2017towards`.

None of that is a refutation. It is a decade of people finding out precisely what the model measures
— which is the process this book is arguing for.

## The lesson that generalizes: specificity has a boundary you did not test

In 2021, a study tested the signature against two conditions nobody had tried: breathlessness, and a
**finger-opposition motor task**. Breathlessness activated it (d = 0.90). The non-aversive motor task
activated it more than anything else tested (d = 1.44). The authors — including the signature's
original senior author — concluded that global signature activity alone is not specific to pain
{cite:p}`harrison2021investigating`.

Look at what had happened. Every specificity test for eight years had compared pain against other
*aversive or emotional* states: anticipation, memory, social rejection, vicarious pain, negative
affect. Within that space the specificity was real and repeatedly confirmed. Nobody had asked whether
someone simply moving their fingers would set it off.

**A model is never "specific". It is specific relative to the alternatives you tested against.** When
you report discriminant validity, report the list of comparisons, so a reader can see what is missing
from it. And when you read someone else's specificity claim, the useful question is not whether the
tests were done well, but which test nobody thought to run.

## Sources

- {cite:t}`wager2013fmri` — the original signature, N = 114 across four studies.
- {cite:t}`woo2014separate`, {cite:t}`krishnan2016somatic`, {cite:t}`chang2015sensitive` — specificity
  against social rejection, vicarious pain and negative affect.
- {cite:t}`harrison2021investigating` — the breathlessness and motor-task counterexample.
- {cite:t}`han2022effect` — within- versus between-person effect sizes and test-retest reliability.
- {cite:t}`zunhammer2018placebo` — placebo analgesia is largely invisible to the signature.
- {cite:t}`woo2017building` — the authors' own framework for developing brain-based biomarkers.
