import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# 1. Cargar datos
df = pd.read_csv("car_prediction_data.csv")

# 2. Separar variables
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# 3. Identificar columnas numéricas y categóricas
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object']).columns

# 4. Preprocesamiento
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(drop="first"), cat_cols)
], remainder="passthrough")

# 5. Pipeline completo (preprocesamiento + modelo)
pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", LinearRegression())
])

# 6. Entrenar
pipeline.fit(X, y)

# 7. Guardar modelo
joblib.dump(pipeline, "modelo_precio_auto.pkl")

print("Modelo entrenado y guardado como modelo_precio_auto.pkl")
