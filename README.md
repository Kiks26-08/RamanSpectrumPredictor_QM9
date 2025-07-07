# Raman Spectrum Predictor (QM9 + ML)
![Tests](https://github.com/naveen-dandu/RamanSpectrumPredictor_QM9/actions/workflows/python-package.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A machine learning pipeline for predicting Raman spectra of organic molecules using RDKit-based molecular descriptors and trained on a QM9-style dataset.

---

## 📂 Project Structure

```
RamanSpectrumPredictor_QM9/
├── data/                # Dataset CSV with features + Raman peaks
├── scripts/             # Training and prediction scripts
├── models/              # Saved ML models
├── notebooks/           # Jupyter notebooks for visualization
├── utils/               # Featurization code using RDKit
├── tests/               # Test scripts (to be added)
└── .github/workflows/   # GitHub Actions CI config
```

---

## 🚀 Quickstart

### 🔧 Create Environment
```bash
conda env create -f environment.yml
conda activate raman-predictor
```

### 🧠 Train the Model
```bash
python scripts/train_model.py
```

### 🔮 Predict Raman Peak from SMILES
```bash
python scripts/predict.py "CCO"
```

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

---
## 📊 Jupyter Notebook (EDA)

To explore the dataset visually:

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```
---

## 🧪 Future Extensions

- Real QM9 parsing with ASE or DeepChem
- GNN-based models with PyTorch Geometric
- SOAP descriptors with DScribe
- Streamlit-based interactive prediction UI

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
DOI: 10.5281/zenodo.15829060
```

See [`CITATION.cff`](CITATION.cff) and [.zenodo.json](.zenodo.json) for full metadata.

---

## 📜 License

[MIT License](https://opensource.org/licenses/MIT)

---

## 🔖 Keywords

`machine-learning` • `raman-spectroscopy` • `qm9` • `chemoinformatics` • `streamlit` • `rdkit` • `xgboost` • `spectral-prediction` • `materials-informatics`

