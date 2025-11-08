Smart Agri 

Pametni sistem za praćenje i predikciju uslova u poljoprivredi.  
Projekat obuhvata Flask backend, React frontend, IoT simulaciju i ML model za analizu podataka.

 Struktura projekta
- **backend/** – Flask API i model
- **frontend/** – korisnički interfejs (React)
- **iot_sim/** – simulacija senzora
- **ml/** – mašinsko učenje i model trening
- **docker-compose.yml** – opcionalno pokretanje u Docker okruženju

Pokretanje (Docker)
*docker-compose up --build

*Frontend (Streamlit) — npr. http://localhost:8501 ili 8502

Pokretanje ručno (bez Dockera) — WSL / Linux / macOS

BACKEND

*cd flask_api

*python3 -m venv venv

*source venv/bin/activate

*pip install -r requirements.txt

*python app.py

FRONTEND

*cd frontend

*python3 -m venv venv

*source venv/bin/activate 

*pip install -r requirements.txt

*streamlit run app.py

IoT simulacija (pokretanje)

*cd iot_sim

*python simulate_sensors.py





