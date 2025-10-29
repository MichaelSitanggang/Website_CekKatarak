import os
import cv2
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

DATASET_PATH = "../../Dataset/train/"
IMG_SIZE = 128

# Load Dataset
X = []
y = []

for label, cls in enumerate(["normal", "katarak",]):
    folder = os.path.join(DATASET_PATH, cls)
    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue  # Skip corrupted image

        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        X.append(img.flatten() / 255.0)
        y.append(label)

X = np.array(X)
y = np.array(y)

# Buat Pipeline PCA + KNN
pipeline = Pipeline([
    ('pca', PCA(n_components=300)),
    ('knn', KNeighborsClassifier(n_neighbors=3)) #setelah dibersihkan coba 5 dan 7 mana paling bagus

])

# Train model
pipeline.fit(X, y)

# Simpan Model
os.makedirs("../model", exist_ok=True)
joblib.dump(pipeline, "../model/model.pkl")

print("✅ Model berhasil dilatih dan disimpan ke backend/model/model.pkl")
print("🚀 Ready untuk digunakan di Flask!")


#bersih bersih dataset
#perbaiki code untuk inputan yang salah 
#pahami code dan selesaikn dokumentasi nya (terakhir)