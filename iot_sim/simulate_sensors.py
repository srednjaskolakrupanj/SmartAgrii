# iot_sim/simulate_sensors.py
import requests
import random
import time

# URL backend servera
url = "http://localhost:5000/send_data"

while True:
    # Simulacija podataka sa senzora
    data = {
        "soil_moisture": random.randint(20, 80),  # vlažnost tla
        "temperature": random.randint(15, 35),    # temperatura
        "humidity": random.randint(40, 80)        # vlažnost vazduha
    }
    
    # Slanje podataka backend-u
    response = requests.post(url, json=data)
    print(response.json())  # prikaz odgovora (True/False za navodnjavanje)
    
    time.sleep(5)  # čekaj 5 sekundi pre sledećeg slanja
