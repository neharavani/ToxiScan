from flask import Flask, request, jsonify
import joblib
import numpy as np
from scipy.sparse import csr_matrix
from flask_cors import CORS



# Load trained model and vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")
nb_ratio = joblib.load("nb_ratio.pkl")
nbsvm_model = joblib.load("nbsvm_model.pkl")

# Initialize Flask app
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "ToxiScan API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # Preprocess text
    text_tfidf = vectorizer.transform([text])
    text_nb = text_tfidf.multiply(nb_ratio)  # Apply NB transformation

    # Predict
    prediction = nbsvm_model.predict(text_nb)[0]
    return jsonify({"toxic": bool(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
