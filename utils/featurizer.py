from rdkit import Chem
from rdkit.Chem import Descriptors

def featurize_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    features = {
        'mol_weight': Descriptors.MolWt(mol),
        'num_atoms': mol.GetNumAtoms(),
        'num_rings': Descriptors.RingCount(mol),
        'polar_surface_area': Descriptors.TPSA(mol),
        'logP': Descriptors.MolLogP(mol)
    }
    return features

def featurize_smiles_list(smiles_list):
    return [featurize_smiles(smile) for smile in smiles_list if featurize_smiles(smile) is not None]
