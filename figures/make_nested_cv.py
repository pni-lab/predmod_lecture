"""Generate contents/5_hyperparameter_optimization/nested_cv.png.

Run from the repository root:  python figures/make_nested_cv.py
"""
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'contents', '5_hyperparameter_optimization', 'nested_cv.png')

TRAIN = '#cfe2f3'
TEST = '#e8934a'
VALIDATION = '#7fb069'
INNER_TRAIN = '#e6e6e6'

fig, ax = plt.subplots(figsize=(11, 6.4))

n_outer, n_inner = 5, 4
block_w, block_h, gap = 1.0, 0.42, 0.18

# ---------------------------------------------------------------- outer loop
outer_top = 0.0
for round_index in range(n_outer):
    y = outer_top - round_index * (block_h + gap)
    for fold in range(n_outer):
        is_test = (fold == round_index)
        ax.add_patch(Rectangle((fold * block_w, y), block_w * 0.97, block_h,
                               facecolor=TEST if is_test else TRAIN,
                               edgecolor='white', lw=1.5))
    ax.text(-0.25, y + block_h / 2, f'round {round_index + 1}', ha='right', va='center', fontsize=9)

ax.text(n_outer * block_w / 2, outer_top + block_h + 0.30,
        'OUTER cross-validation  —  estimates performance', ha='center', fontsize=12, weight='bold')
ax.text(n_outer * block_w / 2, outer_top + block_h + 0.06,
        'the orange fold is never used for anything but scoring the finished model',
        ha='center', fontsize=9, color='0.35')

# ---------------------------------------------------------------- inner loop
inner_top = outer_top - n_outer * (block_h + gap) - 1.25
inner_block_w = block_w * 4 / n_inner   # the 4 non-test outer folds, re-divided into n_inner parts
inner_left = 0.0                        # they are outer round 5's training folds: columns 1-4

for round_index in range(n_inner):
    y = inner_top - round_index * (block_h + gap)
    for fold in range(n_inner):
        is_validation = (fold == round_index)
        ax.add_patch(Rectangle((inner_left + fold * inner_block_w, y), inner_block_w * 0.97, block_h,
                               facecolor=VALIDATION if is_validation else INNER_TRAIN,
                               edgecolor='white', lw=1.5))
    ax.text(inner_left - 0.25, y + block_h / 2, f'round {round_index + 1}',
            ha='right', va='center', fontsize=9)

ax.text(inner_left + 2 * block_w, inner_top + block_h + 0.30,
        'INNER cross-validation  —  chooses the hyperparameters', ha='center',
        fontsize=12, weight='bold')
ax.text(inner_left + 2 * block_w, inner_top + block_h + 0.06,
        'run separately inside every outer round, on that round\'s training data only',
        ha='center', fontsize=9, color='0.35')

# arrow from the training part of the last outer round down into the inner loop
ax.add_patch(FancyArrowPatch((2.0, outer_top - (n_outer - 1) * (block_h + gap) - 0.05),
                             (2.0, inner_top + block_h + 0.62),
                             arrowstyle='-|>', mutation_scale=18, color='0.45', lw=1.5,
                             connectionstyle='arc3,rad=0.0'))
ax.text(2.15, (outer_top - (n_outer - 1) * (block_h + gap) + inner_top + block_h) / 2 + 0.2,
        'the training data of\nthis outer round', fontsize=9, color='0.35', va='center')

# ---------------------------------------------------------------- legend
legend = [(TRAIN, 'training data of the outer round'),
          (TEST, 'test fold: scored once, never seen during tuning or fitting'),
          (INNER_TRAIN, 'training fold of the inner round'),
          (VALIDATION, 'validation fold: used to compare hyperparameter values')]
legend_y = inner_top - n_inner * (block_h + gap) - 0.45
for i, (color, label) in enumerate(legend):
    y = legend_y - i * 0.33
    ax.add_patch(Rectangle((0, y), 0.35, 0.22, facecolor=color, edgecolor='white'))
    ax.text(0.45, y + 0.11, label, va='center', fontsize=9.5)

ax.set_xlim(-1.4, n_outer * block_w + 0.4)
ax.set_ylim(legend_y - len(legend) * 0.33 - 0.1, outer_top + block_h + 0.55)
ax.axis('off')
fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches='tight')
print('wrote', os.path.normpath(OUT))
