# model.py
def predict_irrigation(temperature, humidity, moisture):
    """
    Lažni model koji odlučuje da li treba navodnjavati.
    Kasnije se može zameniti pravim ML modelom.
    """
    if moisture < 35 and temperature > 25 and humidity < 60:
        return "Potrebno navodnjavanje"
    else:
        return "Nije potrebno navodnjavanje"
