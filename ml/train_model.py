# train_model.py
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Simulirani podaci
X = np.random.rand(100, 3)  # soil_moisture, temperature, humidity
y = (X[:, 0] + X[:, 1]*0.5 + X[:, 2]*0.2 > 1).astype(int)  # 0 ili 1 predikcija navodnjavanja

# Kreiranje modela
model = RandomForestClassifier()
model.fit(X, y)

# Čuvanje modela
joblib.dump(model, "model.pkl")
print("Model je napravljen i sačuvan u ml/model.pkl")

import joblib

# Pretpostavimo da tvoj model se zove 'model'
# npr. model = RandomForestClassifier() ili neki drugi
joblib.dump(model, "train_model.pkl")

