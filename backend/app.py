# backend/app.py
from flask import Flask, request, jsonify
import joblib
import datetime

# Učitavanje ML modela
model = joblib.load("../ml/train_model.pkl")

app = Flask(__name__)

@app.route("/send_data", methods=["POST"])
def receive_data():
    data = request.get_json()
    soil = data["soil_moisture"]
    temp = data["temperature"]
    hum = data["humidity"]

    features = [[soil, temp, hum]]
    prediction = model.predict(features)[0]

    return jsonify({
        "timestamp": str(datetime.datetime.now()),
        "recommended_irrigation": bool(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
