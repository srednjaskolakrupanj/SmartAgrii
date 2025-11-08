Smart Agri 

Pametni sistem za praćenje i predikciju uslova u poljoprivredi.  
Projekat obuhvata Flask backend, React frontend, IoT simulaciju i ML model za analizu podataka.

 Struktura projekta
- **backend/** – Flask API i model
- **frontend/** – korisnički interfejs (React)
- **iot_sim/** – simulacija senzora
- **ml/** – mašinsko učenje i model trening
- **docker-compose.yml** – opcionalno pokretanje u Docker okruženju

Preporuceno pokretanje projekta (instalirati Docker na racunaru i pokrenuti ga)

Pokrenut novi prvi WLS 

*cd SmartAgrii

*python3 -m venv venv

*source venv/bin/activate

*docker-compose up --build

Drugi novi WSL - BACKEND

*cd flask_api

*python3 -m venv venv

*source venv/bin/activate

*pip install -r requirements.txt

*python app.py

Treci novi WSL - FRONTEND

*cd frontend

*python3 -m venv venv

*source venv/bin/activate 

*pip install -r requirements.txt

*streamlit run app.py





Poslednji korak:

Pokrenuti pretrazivac na racunaru i uneti: http://localhost:8502 ili http://localhost:8501


