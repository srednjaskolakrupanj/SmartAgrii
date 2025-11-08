Smart Agri 

Pametni sistem za praćenje i predikciju uslova u poljoprivredi.  
Projekat obuhvata Flask backend, React frontend, IoT simulaciju i ML model za analizu podataka.

 Struktura projekta
- **backend/** – Flask API i model
- **frontend/** – korisnički interfejs (React)
- **iot_sim/** – simulacija senzora
- **ml/** – mašinsko učenje i model trening
- **docker-compose.yml** – opcionalno pokretanje u Docker okruženju

Pokretanje backend-a
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py


Pokretanje frontend-a
cd frontend
npm install
npm start


Pokretanje IoT simulacije
cd iot_sim
python simulate_sensors.py

