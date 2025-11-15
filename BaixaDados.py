import yfinance as yf
import pandas as pd



# Escolha o ticker da empresa (ex: Petrobras = PETR4.SA)
ticker = "VALE3.SA"

# Baixar os dados históricos
dados = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Selecionar apenas as colunas desejadas
dados_filtrados = dados["Close"]

# Salvar em CSV
dados_filtrados.to_csv("artefatos/precos_Vale.csv")

# Visualizar os dados
print(dados_filtrados.head())

# Carregar os dados salvos
df = pd.read_csv("artefatos/precos_Vale.csv", index_col="Date", parse_dates=True)

# Verificar valores nulos
print(df.isnull().sum())

# Preencher ou remover nulos
df = df.dropna()
df.to_csv("artefatos/precos_Vale.csv")

# Visualizar estatísticas básicas
print(df.describe())




