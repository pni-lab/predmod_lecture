# The Model That Was Accurate and Wrong

**What it shows: the failure mode that no amount of methodological rigour can detect.**

The two previous examples are neuroimaging studies, and both are about doing predictive modelling
carefully. This one is neither. It is about a model that was done carefully — and caused harm at the
scale of a population.

## The setting

{cite:t}`obermeyer2019dissecting` studied a commercial risk-prediction algorithm used by US health
systems to decide which patients are enrolled in "high-risk care management" programmes: extra
nursing attention, extra appointment slots, coordinated care. Patients above the 97th percentile of
predicted risk were enrolled automatically; those above the 55th were flagged to their physician.
Algorithms of this class are applied, by industry estimates, to about **200 million people a year**.

The algorithm predicted **total health-care costs in the coming year** from insurance claims:
demographics, insurance type, diagnoses, procedures, medications. It did **not** use race as a
feature.

## The finding

At the same risk score, Black patients were substantially sicker than White patients: **26.3% more
chronic conditions** (4.8 versus 3.8), worse blood pressure control, worse diabetic control. Across
the cohort, nearly 49,000 active chronic conditions were invisible to the score. Closing the health
gap at a given score would have raised the share of Black patients receiving the extra help from
**17.7% to 46.5%**.

## Why it happened

The health system wanted to find patients with the greatest **need**. Need is not in the database;
cost is. So cost became the label.

But cost does not measure need — it measures *need that got treated*. For reasons ranging from
transport and time off work to insurance, mistrust and differential treatment by clinicians, about
**$1,800 less per year** was spent on Black patients at an equal number of chronic conditions.

Put the two together. If the model is calibrated on cost, and cost is systematically lower for one
group at equal illness, then equal *predicted cost* necessarily means *unequal illness*. The
disparity is not a bug in the fitting; it is an algebraic consequence of training a good model on a
label carrying a group-dependent offset. The algorithm learned a historical pattern of unequal
treatment and re-expressed it as a prediction of unequal need.

The authors did not change the algorithm. They changed the label — the identical procedure trained
to predict active chronic conditions instead of costs — which removed **84% of the measured bias**
and roughly doubled the share of Black patients auto-enrolled.

## Why this is the most important example in the chapter

Go through this book's checklist. The model passes all of it.

- **Not overfitted.** It held up out of sample.
- **Not leaky.** No implausible performance.
- **Externally validated**, at a scale almost nobody in academic research achieves: the manufacturer
  replicated the analysis on its own national database of **3.7 million patients**.
- **Well calibrated** — and calibrated *equally* across racial groups. At every level of predicted
  risk, Black and White patients went on to incur about the same costs.
- **It did not use the protected attribute at all.**

Cross-validation asks whether your estimate generalizes to new draws from the same distribution.
External validation asks whether it transports to a new site. **Neither asks whether the label was
the right thing to predict** — and neither can, because the quantity actually of interest was never
measured. You cannot cross-validate against a variable that is not in your data.

This is **construct validity**, the part of measurement theory that predictive modelling has been
slowest to import from psychometrics. The internal validity is fine. The external validity is
excellent. The construct validity is broken, and that is invisible from inside the pipeline.

## The diagnostic that did work

Nothing internal to the modelling caught this. What caught it was:

> measuring an outcome the model was **never trained on** — comorbidity counts, blood pressure,
> HbA1c — and examining its distribution **conditional on the model's output**, stratified by a group
> variable **the model never saw**.

That is a general prescription, and it is the practical takeaway of this entire chapter. Audit your
deployed score against an independently measured proxy for the construct you actually care about.
Not against its label. Against the thing you meant.

## The same mistake, elsewhere

The authors list the pattern in other domains, and it is worth keeping the list to hand as a
diagnostic prompt for your own work:

| the construct | the convenient label | what goes wrong |
|---|---|---|
| health need | cost | measures need that got treated |
| hospital quality | readmission rates | penalizes hospitals serving poorer populations |
| creditworthiness | default on past loans | inherits discrimination in employment and lending |
| criminal activity | recorded crime | reflects where police already patrol |
| job performance | supervisor ratings | carries supervisors' biases |

In each row, the model can be flawless and the result still wrong — because the label is not the
construct, and the gap between them is not the same size for everyone.

```{note}
A postscript on regulation. New York's financial and health regulators wrote to the vendor on the
day the paper appeared, demanding it demonstrate the algorithm was not discriminatory or stop using
it. The vendor's defence was that the model predicted cost well — which concedes the paper's entire
argument. Later US rules on discrimination in clinical decision-support tools are framed largely
around tools that *use* protected characteristics as inputs. The canonical case of proxy
discrimination did not use one.
```

## Sources

- {cite:t}`obermeyer2019dissecting` — the study. Synthetic replication data and code are published.
- {cite:t}`obermeyer2021playbook` — the authors' four-step protocol (inventory, screen, retrain,
  prevent) for finding label-choice bias in deployed algorithms.
- {cite:t}`mehrabi2021survey` — a survey of bias and fairness definitions in machine learning.
