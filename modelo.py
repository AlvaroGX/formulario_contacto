import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Entrenamiento sencillo (ejemplo)
def entrenar_modelo():
    data = pd.read_csv("datos.csv")
    X = data[["habitaciones", "superficie"]]
    y = data["precio"]

    modelo = LinearRegression()
    modelo.fit(X, y)
    joblib.dump(modelo, "modelo_casas.pkl")

def predecir(habitaciones, superficie, ubicacion="centro"):
    try:
        modelo = joblib.load("modelo_casas.pkl")
    except:
        entrenar_modelo()
        modelo = joblib.load("modelo_casas.pkl")

    prediccion = modelo.predict([[habitaciones, superficie]])
    return round(prediccion[0], 2)