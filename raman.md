# 🔬 Raman Spectrum Predictor (QM9 + ML)

![Tests](https://github.com/naveen-dandu/RamanSpectrumPredictor_QM9/actions/workflows/python-package.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning pipeline that predicts Raman spectral peak positions near 1600 cm⁻¹ for organic molecules using RDKit descriptors trained on a QM9-like dataset.  
Includes CLI tools, a Streamlit web app, Jupyter notebooks for EDA, and GitHub Actions integration.

---

## 🧠 Features

- ✅ RDKit-based molecular featurization
- ✅ XGBoost regression model
- ✅ CLI scripts for training and prediction
- ✅ Streamlit UI for interactive use
- ✅ Jupyter notebook for data exploration
- ✅ Pytest and GitHub Actions for continuous integration
- ✅ Zenodo/DOI-ready metadata and citation support

---

## 📂 Project Structure

```
RamanSpectrumPredictor_QM9/
├── app.py                  # Streamlit UI
├── data/                   # QM9-style training data
├── docs/                   # Usage and documentation
├── models/                 # Trained ML models
├── notebooks/              # Jupyter EDA and visualizations
├── scripts/                # Training and prediction scripts
├── tests/                  # Pytest unit tests
├── utils/                  # RDKit featurizer
├── .github/workflows/      # GitHub Actions CI
├── requirements.txt        # Python dependencies
├── environment.yml         # Conda environment
├── .zenodo.json            # Zenodo metadata
├── CITATION.cff            # GitHub citation file
└── README.md
```

---

## ⚙️ Setup

### Using Conda

```bash
conda env create -f environment.yml
conda activate raman-predictor
```

### Using Pip

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Train the Model

```bash
python scripts/train_model.py
```

### Predict from SMILES

```bash
python scripts/predict.py "CCO"
```

### Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Jupyter Notebook (EDA)

To explore the dataset visually:

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

On HPC:
```bash
jupyter notebook --no-browser --port=8888
# Tunnel from local machine:
ssh -N -L 8888:localhost:8888 user@hpc
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📄 Citation

If you use this work, please cite:

```yaml
Dandu, Naveen. RamanSpectrumPredictor_QM9. 2025. 
DOI: 10.5281/zenodo.1234567
```

See [`CITATION.cff`](CITATION.cff) and [.zenodo.json](.zenodo.json) for full metadata.

---

## 📜 License

[MIT License](https://opensource.org/licenses/MIT)

---

## 🔖 Keywords

`machine-learning` • `raman-spectroscopy` • `qm9` • `chemoinformatics` • `streamlit` • `rdkit` • `xgboost` • `spectral-prediction` • `materials-informatics`
