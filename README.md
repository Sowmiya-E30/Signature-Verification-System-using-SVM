# ✍️ Signature Verification System

A machine learning-based **Signature Verification System** that determines whether a given signature is **genuine or forged**. The project uses **image processing techniques and a Support Vector Machine (SVM)** classifier to analyze signature images and make predictions.

## 📌 Project Overview

Signature verification is an important application of image processing and machine learning, especially in areas such as banking, document authentication, and identity verification.

This project takes a signature image as input, processes the image using computer vision techniques, extracts relevant features, and uses a trained **SVM model** to classify the signature.

The application provides a simple **Streamlit web interface** where users can upload a signature image and obtain the verification result.

## 🚀 Features

* Upload a signature image through a web interface
* Image preprocessing using OpenCV
* Feature extraction using image-processing techniques
* Signature classification using a trained SVM model
* Displays the verification result through Streamlit
* Simple and user-friendly interface
* Trained model stored using Joblib

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web application interface
* **OpenCV** – Image processing
* **NumPy** – Numerical operations
* **Scikit-image** – Image feature processing
* **Scikit-learn** – Machine learning and SVM classification
* **Joblib** – Saving and loading the trained model
* **Jupyter Notebook** – Model development and experimentation

## 🧠 Machine Learning Model

The project uses a **Support Vector Machine (SVM)** for signature classification.

The general workflow is:

```text
Signature Image
       ↓
Image Preprocessing
       ↓
Feature Extraction
       ↓
Feature Representation
       ↓
Trained SVM Model
       ↓
Prediction
       ↓
Genuine / Forged
```

## 📂 Project Structure

```text
Signature-Verification/
│
├── app.py
├── svm.ipynb
├── svm_signature_model.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                      | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| `app.py`                  | Streamlit application used to run the signature verification system     |
| `svm.ipynb`               | Jupyter Notebook containing the machine learning/model development work |
| `svm_signature_model.pkl` | Trained SVM model                                                       |
| `requirements.txt`        | Python dependencies required to run the project                         |
| `README.md`               | Project documentation                                                   |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Signature-Verification
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

The project requires Streamlit, Joblib, OpenCV, NumPy, Scikit-image, and Scikit-learn.

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the Streamlit URL displayed in the terminal.

## 🖼️ How to Use

1. Launch the Streamlit application.
2. Upload a signature image.
3. The application processes the uploaded image.
4. Features are extracted from the signature.
5. The trained SVM model analyzes the extracted features.
6. The system displays the predicted verification result.

## 📊 Model Development

The `svm.ipynb` notebook is used for the machine learning workflow, including the development and training of the SVM-based signature verification model.

The trained model is saved as:

```text
svm_signature_model.pkl
```

The saved model is loaded by the Streamlit application for making predictions on new signature images.

## 📦 Requirements

The main dependencies include:

```text
streamlit
joblib
opencv-python
numpy
scikit-image
scikit-learn
```

Exact package versions are specified in `requirements.txt`.

## 🔮 Future Improvements

* Improve verification accuracy using a larger signature dataset
* Add advanced feature extraction techniques
* Compare SVM with deep learning models such as CNNs
* Add support for multiple signature samples per user
* Improve the user interface
* Add confidence scores for predictions
* Deploy the application as an online service

## 🎯 Applications

Signature verification systems can be useful in:

* Banking and financial document verification
* Legal document authentication
* Identity verification
* Digital document processing
* Automated form verification
* Fraud detection systems

## 👩‍💻 Author

**Sowmiya Emarose**

B.Tech – Computer Science Engineering
Artificial Intelligence & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
