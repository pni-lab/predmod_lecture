"""Generate contents/4_reducing_complexity/pca.png.

Run from the repository root:  python figures/make_pca.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'contents', '4_reducing_complexity', 'pca.png')
DATA = os.path.join(HERE, '..', 'ex_data', 'IXI', 'ixi.csv')

# two strongly correlated real features: the same region in the two hemispheres
COLUMNS = ['lh_superiorfrontal_volume', 'rh_superiorfrontal_volume']

df = pd.read_csv(DATA).sample(frac=1, random_state=42).reset_index(drop=True)
X = StandardScaler().fit_transform(df[COLUMNS])

pca = PCA(n_components=2).fit(X)
scores = pca.transform(X)
explained = pca.explained_variance_ratio_ * 100

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

# ---------------------------------------------------------------- original space
ax = axes[0]
ax.scatter(X[:, 0], X[:, 1], s=14, alpha=0.45, color='#1f77b4')
for i, (length, vector) in enumerate(zip(pca.explained_variance_, pca.components_)):
    end = vector * np.sqrt(length) * 2.2
    ax.annotate('', xy=end, xytext=(0, 0),
                arrowprops=dict(arrowstyle='-|>', lw=2.2, color='#d62728', shrinkA=0, shrinkB=0))
    # push the label clear of the arrow tip, along the component's own direction
    label_at = end + vector / np.linalg.norm(vector) * 1.15
    ax.text(*label_at, f'PC{i + 1}\n{explained[i]:.0f}% of variance',
            color='#d62728', fontsize=9.5, ha='center', va='center')
ax.set_xlabel('left superior frontal volume (standardized)')
ax.set_ylabel('right superior frontal volume (standardized)')
ax.set_title('Two correlated features')
ax.set_aspect('equal')
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-4.2, 4.2)

# ---------------------------------------------------------------- component space
ax = axes[1]
ax.scatter(scores[:, 0], scores[:, 1], s=14, alpha=0.45, color='#2ca02c')
ax.axhline(0, color='0.8', lw=1)
ax.axvline(0, color='0.8', lw=1)
ax.set_xlabel(f'PC1  ({explained[0]:.0f}% of variance)')
ax.set_ylabel(f'PC2  ({explained[1]:.0f}%)')
ax.set_title('The same data, in component coordinates')
ax.set_aspect('equal')
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-4.2, 4.2)

for ax in axes:
    ax.spines[['top', 'right']].set_visible(False)

fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches='tight')
print('wrote', os.path.normpath(OUT))
print('explained variance ratio:', np.round(pca.explained_variance_ratio_, 4))
print('correlation of the two features:', round(np.corrcoef(X.T)[0, 1], 3))
