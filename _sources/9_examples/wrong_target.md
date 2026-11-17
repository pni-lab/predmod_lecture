# The Model That Was Accurate and Wrong

**What it shows: the failure mode that no amount of methodological rigour can detect.**

The two previous examples are neuroimaging studies, and both are about doing predictive modelling
carefully. This one is about a model that was also done carefully, and that caused harm at the scale
of a population.

## The setting

{cite:t}`obermeyer2019dissecting` studied a commercial risk-prediction algorithm used by US health
systems to decide which patients are enrolled in "high-risk care management" programmes: extra
nursing attention, extra appointment slots, coordinated care. Patients above the 97th percentile of
predicted risk were enrolled automatically, and those above the 55th were flagged to their physician.
Algorithms of this class are applied, by industry estimates, to about **200 million people a year**.

The algorithm predicted **total health-care costs in the coming year** from insurance claims:
demographics, insurance type, diagnoses, procedures, medications. It did **not** use race as a
feature.

## The finding

At the same risk score, Black patients were substantially sicker than White patients: **26.3% more
chronic conditions** (4.8 versus 3.8), worse blood pressure control, worse diabetic control. Closing
the health gap at a given score would have raised the share of Black patients receiving the extra
help from **17.7% to 46.5%**. The manufacturer repeated the analysis on its own national database of
**3.7 million** insured patients and confirmed the finding.

## The mechanism

The health system wanted to find the patients with the greatest **need**. Need is not recorded in the
database, whereas cost is, so cost became the label.

Cost, however, measures *need that got treated*. For reasons ranging from transport and time off work
to insurance, mistrust and differential treatment by clinicians, about **$1,800 less per year** was
spent on Black patients at an equal number of chronic conditions.

Putting the two together: if the model is calibrated on cost, and cost is systematically lower for
one group at equal illness, then equal *predicted cost* necessarily means *unequal illness*. The
disparity is an algebraic consequence of training a good model on a label that carries a
group-dependent offset, rather than a bug in the fitting. The algorithm learned a historical pattern
of unequal treatment and re-expressed it as a prediction of unequal need.

The authors did not change the algorithm, they changed the label. The identical procedure trained to
predict active chronic conditions instead of costs **roughly doubled** the share of Black patients
auto-enrolled, from 14.1% to 26.7%. A further variant predicting a combined health-and-cost index cut
their measure of bias (the excess chronic conditions carried by Black patients at equal risk score)
by **84%**.

## Performance against the book's checklist

Going through this book's checklist, the model passes all of it.

- **Not overfitted.** It held up out of sample, and was deployed at national scale.
- **Not leaky.** No implausible performance.
- **Well calibrated** on the quantity it predicted, and calibrated *equally* across racial groups: at
  every level of predicted risk, Black and White patients went on to incur about the same costs.
- **It did not use the protected attribute at all.**
- **Its behaviour reproduced** in an independent national database of 3.7 million patients.

An external validation would have passed it as well. Take the model to a new hospital, compare
predicted with actual costs, and it predicts costs well there too, because it does predict costs
well. Every validation available to us validates the model against its label.

Cross-validation asks whether an estimate generalizes to new draws from the same distribution, and
external validation asks whether it transports to a new site. **Neither asks whether the label was
the right thing to predict**, and neither can, because the quantity actually of interest was never
measured. A variable that is not in the data cannot be cross-validated against.

This is **construct validity**, the part of measurement theory that predictive modelling has been
slowest to import from psychometrics. The internal validity is fine and the external validity is
excellent, while the construct validity is broken, and that is invisible from inside the pipeline.

## The diagnostic that worked

Nothing internal to the modelling caught this. What caught it was:

> measuring an outcome the model was **never trained on** (comorbidity counts, blood pressure,
> HbA1c) and examining its distribution **conditional on the model's output**, stratified by a group
> variable **the model never saw**.

That is a general prescription, and it is the practical takeaway of this entire chapter. Audit a
deployed score against an independently measured proxy for the construct of interest, rather than
against its label.

## The same pattern in other domains

The authors list the pattern elsewhere, and the list is worth keeping to hand as a diagnostic prompt:

| the construct | the convenient label | what goes wrong |
|---|---|---|
| health need | cost | measures need that got treated |
| hospital quality | readmission rates | penalizes hospitals serving poorer populations |
| creditworthiness | default on past loans | inherits discrimination in employment and lending |
| criminal activity | recorded crime | reflects where police already patrol |
| job performance | supervisor ratings | carries supervisors' biases |

In each row the model can be flawless and the result still wrong, because the label is not the
construct, and the gap between them is not the same size for everyone.

```{note}
A postscript on regulation. New York's financial and health regulators wrote to the vendor on the
day the paper appeared, demanding it demonstrate the algorithm was not discriminatory or stop using
it. The vendor's defence was that the model predicted cost well, which concedes the paper's entire
argument. Later US rules on discrimination in clinical decision-support tools are framed largely
around tools that *use* protected characteristics as inputs, whereas the canonical case of proxy
discrimination did not use one.
```

## Sources

- {cite:t}`obermeyer2019dissecting`: the study. Synthetic replication data and code are published.
- {cite:t}`obermeyer2021playbook`: the authors' four-step protocol (inventory, screen, retrain,
  prevent) for finding label-choice bias in deployed algorithms.
- {cite:t}`mehrabi2021survey`: a survey of bias and fairness definitions in machine learning.
