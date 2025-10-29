import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import joblib
import numpy as np
import cv2

MODEL_PATH = "model/model.pkl"
pipeline = joblib.load(MODEL_PATH)
pipeline.named_steps["knn"].n_jobs = 1 

IMG_SIZE = 128
LABELS = ["Normal", "Katarak"]

def predict_image(file_stream):
    import cv2, numpy as np

    # Baca file stream menjadi array
    file_bytes = np.frombuffer(file_stream.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return "Gambar tidak bisa dibaca", 0.0
    
    img = cv2.equalizeHist(img)
    # Preprocessing (resize + flatten + normalisasi)
    img = cv2.resize(img, (128, 128))
    img_flat = img.flatten().reshape(1, -1)
    img_flat = img_flat / 255.0  # normalisasi optional

    # Prediksi
    pred = pipeline.predict(img_flat)[0]
    proba = pipeline.predict_proba(img_flat)[0]
    confidence = np.max(proba)

    # Jika confidence < threshold → input salah
    if confidence < 0.6:
        return "Input bukan gambar retina yang valid", confidence

    LABELS = ["Normal", "Katarak"]
    return LABELS[pred], confidence

