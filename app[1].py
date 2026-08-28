import cv2
import joblib
import numpy as np
import sklearn
import streamlit as st
from skimage.feature import hog

# Load trained model
model = joblib.load("svm_signature_model.pkl")

st.title("Signature Verification System")

if sklearn.__version__ != "1.6.1":
    st.warning(
        f"This model was trained with scikit-learn 1.6.1, but the current "
        f"environment is using {sklearn.__version__}. Predictions may be unreliable."
    )

# Upload image
uploaded_file = st.file_uploader("Upload Signature Image", type=["jpg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 0)

    # Resize (same as training)
    img = cv2.resize(img, (128, 64))

    # Extract HOG features
    features = hog(img, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    features = features.reshape(1, -1)

    # Predict
    prediction = model.predict(features)

    if prediction[0] == 0:
        st.success("Genuine Signature")
    else:
        st.error("Forged Signature")

    st.image(img, caption="Uploaded Image", use_container_width=True)
