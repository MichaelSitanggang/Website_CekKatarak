from flask import Blueprint, jsonify, request
from .model import predict_image

bp = Blueprint("api", __name__)

@bp.route("/", methods=["GET"])
def home():
    return "Cataract Classification API Running!"

@bp.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "Image not found"}), 400

    file = request.files["image"]
    label, score = predict_image(file)
    return jsonify({"label": label, "confidence": float(score)})

