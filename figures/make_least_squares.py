"""Generate contents/2_linear_models/least_squares.png.

Run from the repository root:  python figures/make_least_squares.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'contents', '2_linear_models', 'least_squares.png')
DATA = os.path.join(HERE, '..', 'ex_data', 'IXI', 'ixi.csv')

df = pd.read_csv(DATA).sample(n=30, random_state=42).reset_index(drop=True)
x = df['Age'].values
y = df['rh_superiorfrontal_volume'].values / 1000.0   # cm3, so the axis is readable

# least squares solution
slope, intercept = np.polyfit(x, y, 1)
yhat = intercept + slope * x

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
for xi, yi, yi_hat in zip(x, y, yhat):
    ax.plot([xi, xi], [yi, yi_hat], color='0.6', lw=1, zorder=1)
ax.scatter(x, y, s=28, color='#1f77b4', zorder=3, label='observed $y_i$')
xs = np.array([x.min() - 2, x.max() + 2])
ax.plot(xs, intercept + slope * xs, color='#d62728', lw=2, zorder=2,
        label=r'fitted line $\beta_0 + \beta_1 x$')
ax.plot([], [], color='0.6', lw=1, label=r'residuals $\varepsilon_i$')
ax.set_xlabel('age (years)')
ax.set_ylabel('right superior frontal volume (cm$^3$)')
ax.set_title('Residuals of a fitted line')
ax.legend(frameon=False, loc='upper right', fontsize=9)

ax = axes[1]
slopes = np.linspace(slope - 0.35, slope + 0.35, 400)
# for each candidate slope, use the intercept that is optimal for it
sse = [np.sum((y - (np.mean(y) - s * np.mean(x)) - s * x) ** 2) for s in slopes]
ax.plot(slopes, sse, color='#d62728', lw=2)
ax.axvline(slope, color='0.6', ls='--', lw=1)
ax.scatter([slope], [np.sum((y - yhat) ** 2)], color='#d62728', zorder=5)
ax.annotate('least squares\nsolution', xy=(slope, np.sum((y - yhat) ** 2)),
            xytext=(slope + 0.07, np.sum((y - yhat) ** 2) + 0.35 * (max(sse) - min(sse))),
            fontsize=10, color='0.3',
            arrowprops=dict(arrowstyle='->', color='0.5'))
ax.set_xlabel(r'slope $\beta_1$')
ax.set_ylabel(r'$\sum \varepsilon_i^2$')
ax.set_title('Sum of squared residuals')

for ax in axes:
    ax.spines[['top', 'right']].set_visible(False)

fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches='tight')
print('wrote', os.path.normpath(OUT))
