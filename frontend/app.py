import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="Smart Agriculture Dashboard", page_icon="🌱")

st.title("🌱 Smart Agriculture Dashboard")
st.write("Podaci u realnom vremenu sa Flask API-ja (test verzija)")

# Čuvamo istoriju podataka
data_history = []

placeholder = st.empty()

while True:
    try:
        response = requests.get("http://127.0.0.1:5001/data")
        if response.status_code == 200:
            data = response.json()

            # Dodajemo trenutne vrednosti u istoriju
            data["time"] = time.strftime("%H:%M:%S")
            data_history.append(data)

            # Prikaz trenutnih vrednosti
            with placeholder.container():
                st.subheader("🌡️ Temperatura")
                st.metric(label="", value=f"{data['temperature']} °C")

                st.subheader("💧 Vlažnost vazduha")
                st.metric(label="", value=f"{data['humidity']} %")

                st.subheader("🌿 Vlažnost zemljišta")
                st.metric(label="", value=f"{data['moisture']} %")
                st.write(f"💧 **Status navodnjavanja:** {data['prediction']}")


                # Ako imamo više od 2 merenja — prikaži graf
                if len(data_history) > 2:
                    df = pd.DataFrame(data_history)
                    fig = px.line(
                        df,
                        x="time",
                        y=["temperature", "humidity", "moisture"],
                        labels={"value": "Vrednost", "time": "Vreme", "variable": "Parametar"},
                        title="📊 Promene parametara u realnom vremenu"
                    )
                    st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("Nema podataka sa Flask API-ja")

    except Exception as e:
        st.error(f"Greška: {e}")

    time.sleep(5)  # osvežavanje svakih 5 sekundi


