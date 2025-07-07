import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import joblib
from utils.featurizer import featurize_smiles

def load_model(path='models/best_model.pkl'):
    return joblib.load(path)

def predict(smiles, model):
    features = featurize_smiles(smiles)
    if features is None:
        print("Invalid SMILES input.")
        return
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    print(f"Predicted Raman peak (~1600 cm⁻¹): {prediction:.2f} cm⁻¹")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py 'CCO'")
    else:
        smiles_input = sys.argv[1]
        model = load_model()
        predict(smiles_input, model)
