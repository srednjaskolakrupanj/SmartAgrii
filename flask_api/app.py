from flask import Flask, jsonify
from flask_cors import CORS
import random
from model import predict_irrigation   # ⬅ uvoz modela

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_data():
    temperature = round(random.uniform(18.0, 30.0), 1)
    humidity = round(random.uniform(40.0, 80.0), 1)
    moisture = round(random.uniform(20.0, 60.0), 1)

    # 🔹 poziv ML modela
    prediction = predict_irrigation(temperature, humidity, moisture)

    data = {
        "temperature": temperature,
        "humidity": humidity,
        "moisture": moisture,
        "prediction": prediction
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


