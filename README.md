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

## 📈 Features

- RDKit-based featurization: mol_weight, ring count, TPSA, logP, etc.
- XGBoost regression model
- Modular scripts for training and prediction
- Jupyter notebook support for exploration
- GitHub Actions for CI/CD

---

## 🧪 Future Extensions

- Real QM9 parsing with ASE or DeepChem
- GNN-based models with PyTorch Geometric
- SOAP descriptors with DScribe
- Streamlit-based interactive prediction UI

---

## 🧾 License

MIT License
