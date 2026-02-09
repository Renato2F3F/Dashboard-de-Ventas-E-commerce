# scripts/01_clean_data.py
import pandas as pd

df = pd.read_csv("data/raw/sales_raw.csv")

# Convertir fecha
df["date"] = pd.to_datetime(df["date"])

# Crear columna total
df["total"] = df["price"] * df["quantity"]

# Quitar nulos
df = df.dropna()

df.to_csv("data/processed/sales_clean.csv", index=False)
print("✔ Datos limpiados y guardados.")
