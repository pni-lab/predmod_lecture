# A Gentle Introduction to Predictive Modelling
### A Jupyter Book

[![GitHub license](https://img.shields.io/github/license/pni-lab/predmod_lecture.svg)](https://github.com/pni-lab/predmod_lecture/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/pni-lab/predmod_lecture.svg)](https://github.com/pni-lab/predmod_lecture/releases/)
[![GitHub issues](https://img.shields.io/github/issues/pni-lab/predmod_lecture.svg)](https://github.com/pni-lab/predmod_lecture/issues/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pni-lab/predmod_lecture/master)

**Read the book [here](https://pni-lab.github.io/predmod_lecture).**

An interactive introduction to predictive modelling and machine learning for biomedical
researchers, developed through a single running example: predicting age from cortical structure in
the [IXI](https://brain-development.org/ixi-dataset/) dataset.

## Running the notebooks

Every practice page is a Jupyter notebook and can be run in the cloud from the book itself (the
rocket icon at the top of each page opens it in Binder or Colab), or locally:

```bash
git clone https://github.com/pni-lab/predmod_lecture.git
cd predmod_lecture
pip install -r requirements.txt
jupyter lab contents/
```

## Building the book

```bash
pip install -r requirements.txt
jupyter-book build contents/
```

The result is written to `contents/_build/html/`. Notebook outputs are committed to the
repository, so the build itself does not execute anything. The notebooks are re-executed in
continuous integration (`.github/workflows/book.yml`), which is what keeps those committed outputs
trustworthy: if a notebook stops running, the build fails, and if its outputs drift from what is
committed, the run reports it.

To re-execute everything locally:

```bash
jupyter nbconvert --to notebook --execute --inplace contents/*/*.ipynb
```

## Repository layout

| path | contents |
|---|---|
| `contents/` | the book: one directory per chapter, plus `_toc.yml` and `_config.yml` |
| `ex_data/IXI/` | the example dataset (cortical volumes and age, n=638) |
| `figures/` | scripts that generate the static figures used in the text |

## Data

The example data is derived from the [IXI dataset](https://brain-development.org/ixi-dataset/),
processed with [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) to give volumes of the 68
Desikan-Killiany cortical regions {cite:p}`desikan2006automated`. IXI is made available under
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); please acknowledge the source if
you use it.

## Contributing

Corrections and suggestions are very welcome — please open an
[issue](https://github.com/pni-lab/predmod_lecture/issues/new).

## License

The book is licensed under [CC BY-SA 4.0](LICENSE), matching the share-alike terms of the IXI data
it builds on. Code samples may additionally be used under the MIT license.
