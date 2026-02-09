# scripts/02_kpi_analysis.py
import pandas as pd

df = pd.read_csv("data/processed/sales_clean.csv")

kpis = {
    "total_sales": df["total"].sum(),
    "total_orders": df["order_id"].nunique(),
    "top_product": df.groupby("product")["total"].sum().idxmax()
}

print("📊 KPIs:")
for k, v in kpis.items():
    print(f"{k}: {v}")
