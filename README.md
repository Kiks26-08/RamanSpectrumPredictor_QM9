# Raman Spectrum Predictor: ML Model for QM9 Molecules

![Raman Spectrum Predictor](https://img.shields.io/badge/Raman%20Spectrum%20Predictor-QM9-blue?style=flat&logo=github)

## Overview

The **Raman Spectrum Predictor** is a machine learning model designed to estimate Raman peak positions for QM9-like molecules, particularly around 1600 cm⁻¹. This repository includes a complete training pipeline, a user-friendly Streamlit interface, and RDKit-based featurization methods. 

### Features

- **Machine Learning Model**: Trained specifically on QM9-like molecules to provide accurate predictions.
- **Streamlit UI**: An interactive web interface for users to visualize and interact with the model's predictions.
- **RDKit Featurization**: Utilizes RDKit for molecular featurization, ensuring robust data representation.
- **Training Pipeline**: Comprehensive scripts to train and evaluate the model efficiently.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Streamlit Interface](#streamlit-interface)
- [Featurization](#featurization)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)

## Installation

To set up the Raman Spectrum Predictor on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kiks26-08/RamanSpectrumPredictor_QM9.git
   cd RamanSpectrumPredictor_QM9
   ```

2. **Install Required Packages**:
   Use `pip` to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup RDKit**:
   Follow the [RDKit installation instructions](https://www.rdkit.org/docs/Install.html) to ensure you have RDKit set up correctly in your environment.

## Usage

### Running the Streamlit Interface

To start the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will launch a web browser window where you can input molecular data and visualize Raman peak predictions.

### Making Predictions

Once the Streamlit app is running, you can:

1. Input the molecular structure using SMILES notation.
2. Click on the "Predict" button.
3. View the predicted Raman peaks displayed on the interface.

### Example Input

For example, you can use the SMILES representation for benzene:

```
C1=CC=CC=C1
```

## Model Training

### Dataset

The model is trained on a dataset derived from QM9, which contains a diverse set of molecular structures. Ensure you have the dataset in the correct format before training.

### Training Process

1. **Prepare the Data**: Use the provided scripts in the `data_preparation` directory to clean and format your dataset.
2. **Train the Model**:
   ```bash
   python train_model.py --data_path path/to/your/dataset.csv
   ```

3. **Evaluate the Model**: After training, evaluate the model's performance using:
   ```bash
   python evaluate_model.py --model_path path/to/your/model
   ```

## Streamlit Interface

The Streamlit interface provides an intuitive way to interact with the model. It allows users to input molecular structures and visualize predictions without needing extensive programming knowledge.

### Key Components

- **Input Field**: For entering SMILES strings.
- **Prediction Button**: To trigger the model's prediction.
- **Results Display**: Shows predicted Raman peaks and their intensities.

![Streamlit Interface](https://img.shields.io/badge/Streamlit%20Interface-Interactive%20UI-orange?style=flat)

## Featurization

The model uses RDKit for molecular featurization. This step transforms the molecular data into a format suitable for machine learning.

### RDKit Features

- **Molecular Descriptors**: Various descriptors are calculated to represent molecular properties.
- **Fingerprint Generation**: Generates fingerprints for similarity calculations.

## Contributing

We welcome contributions from the community. If you want to help improve the Raman Spectrum Predictor, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the repository page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

For the latest updates and downloadable files, please visit the [Releases](https://github.com/Kiks26-08/RamanSpectrumPredictor_QM9/releases) section of this repository. You can download the latest version and execute it to get started.

![Download Releases](https://img.shields.io/badge/Download%20Latest%20Release-Click%20Here-green?style=flat&logo=github)

Check the releases section for any updates or changes to the model.