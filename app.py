import streamlit as st
import pandas as pd
import joblib
from utils.featurizer import featurize_smiles

st.title("🔬 Raman Spectrum Predictor (QM9 + ML)")
st.write("Enter a SMILES string to predict its Raman peak near 1600 cm⁻¹.")

# User input
smiles_input = st.text_input("Enter SMILES", "CCO")

# Load model
@st.cache_resource
def load_model(path='models/best_model.pkl'):
    return joblib.load(path)

model = load_model()

# Prediction
if smiles_input:
    features = featurize_smiles(smiles_input)
    if features:
        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]
        st.success(f"Predicted Raman peak: **{prediction:.2f} cm⁻¹**")
        st.write("Features used for prediction:")
        st.json(features)
    else:
        st.error("Invalid SMILES input. Please try again.")
