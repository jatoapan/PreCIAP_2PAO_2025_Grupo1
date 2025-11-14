import joblib
import pandas as pd

# 1. Cargar el modelo guardado
modelo = joblib.load("modelo_precio_auto.pkl")

# 2. Crear los datos nuevos a predecir
# Ejemplo:
datos_nuevos = pd.DataFrame({
    "Year": [2017],
    "Present_Price": [5.6],
    "Kms_Driven": [35000],
    "Fuel_Type": ["Petrol"],
    "Seller_Type": ["Individual"],
    "Transmission": ["Manual"],
    "Owner": [0]
})

# 3. Hacer predicción
prediccion = modelo.predict(datos_nuevos)

print("Precio estimado:", prediccion[0])
