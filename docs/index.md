# Usage Documentation

## 🧠 Training
To train the model on QM9-style features:

```bash
python scripts/train_model.py
```

## 🔮 Prediction
To predict the Raman peak (near 1600 cm⁻¹) for a given molecule:

```bash
python scripts/predict.py "CCO"
```

## 🌐 Streamlit UI
Launch locally with:

```bash
streamlit run app.py
```

Or visit the deployed Streamlit Cloud app once published.
