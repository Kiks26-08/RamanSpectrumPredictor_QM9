from utils.featurizer import featurize_smiles

def test_featurize_smiles_valid():
    features = featurize_smiles("CCO")  # Ethanol
    assert isinstance(features, dict)
    assert "mol_weight" in features
    assert features["mol_weight"] > 0

def test_featurize_smiles_invalid():
    features = featurize_smiles("INVALID")
    assert features is None
