import pandas as pd
from prophet import Prophet
import joblib
import os

df = pd.read_csv("artefatos/precos_Vale.csv", parse_dates=True)  # ou parse_dates=["Date"] se a coluna for "Date"
print("Colunas originais:", df.columns.tolist())

# Ajuste os nomes originais conforme o seu CSV.
# Exemplo: se a coluna de data for "Date" e a de preço for "VALE3.SA" ou "Close"
orig_date = "Date"         # substitua se necessário
orig_close = "VALE3.SA"    # substitua por "Close" se for esse o caso

if orig_date not in df.columns or orig_close not in df.columns:
    raise KeyError(f"Colunas esperadas não encontradas: {orig_date}, {orig_close}")

df_prophet = df.rename(columns={orig_date: "ds", orig_close: "y"})[["ds", "y"]]
df_prophet["ds"] = pd.to_datetime(df_prophet["ds"])
df_prophet = df_prophet.dropna().sort_values("ds")  # ordenar por data

# Treinar e salvar (exemplo)
modelo = Prophet()
modelo.fit(df_prophet)
os.makedirs("artefatos", exist_ok=True)
joblib.dump(modelo, "artefatos/modelo_prophet.pkl", compress=3)
print("Modelo salvo.")
