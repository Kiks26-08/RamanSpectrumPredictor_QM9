import pandas as pd
from xgboost import XGBRegressor
from utils.featurizer import featurize_smiles

def test_model_prediction():
    # Train a mock model on dummy data
    X = pd.DataFrame([featurize_smiles("CCO")])
    y = [1600.0]
    model = XGBRegressor(n_estimators=10)
    model.fit(X, y)

    # Predict
    prediction = model.predict(X)[0]
    assert 1500 <= prediction <= 1700
