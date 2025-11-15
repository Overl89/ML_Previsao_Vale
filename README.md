
# 📊 Documentação do Projeto: Previsão de Fechamento de Ações da Vale com MLOps

## 1. 🎯 Objetivo do Projeto
Desenvolver um modelo preditivo para estimar o preço de fechamento das ações da empresa Vale (VALE3), utilizando dados históricos da bolsa de valores e técnicas de séries temporais. O projeto inclui a aplicação de práticas de MLOps para garantir reprodutibilidade, escalabilidade e monitoramento contínuo.

## 2. 🏢 Empresa Escolhida
- **Empresa:** Vale S.A.
- **Ticker:** VALE3
- **Bolsa:** B3 (Brasil)

## 3. 📈 Coleta de Dados
- **Fonte:** Yahoo Finance via `yfinance`
- **Período:** Janeiro de 2020 a Dezembro de 2024
- **Features utilizadas:**
  - Data
  - Preço de abertura
  - Preço de fechamento
  - Máxima, mínima
  - Volume negociado

## 4. 🧠 Algoritmo de Machine Learning
- **Algoritmo:** Prophet (Facebook)
- **Justificativa:** Prophet é robusto para séries temporais com sazonalidade e tendência, além de lidar bem com dados faltantes e mudanças abruptas.
- **Pré-processamento:**
  - Renomeação de colunas para o formato exigido pelo Prophet (`ds` e `y`)
  - Conversão de datas
  - Filtragem de outliers

## 5. 📊 Avaliação do Modelo
- **Métricas utilizadas:**
  - MAE (Erro Absoluto Médio)
  - RMSE (Raiz do Erro Quadrático Médio)
  - MAPE (Erro Percentual Absoluto Médio)
- **Resultados:**
  - MAE: 1.85
  - RMSE: 2.47
  - MAPE: 3.2%

## 6. 📦 Serialização do Modelo
- **Ferramenta:** `joblib`
- **Arquivo gerado:** `modelo_prophet.pkl`

## 7. 🧪 Ambiente Virtual
- **Gerenciado com:** `Docker`
- **Arquivo de dependências:** `requirements.txt`
- **Principais bibliotecas:**
  - pandas
  - numpy
  - prophet
  - fastapi
  - uvicorn
  - joblib

## 8. 🌐 API de Predição
- **Framework:** FastAPI
- **Deploy:** Hugging Face Spaces
- **Endpoints:**
  - `POST /predict`: recebe uma data futura e retorna a previsão de fechamento
- **Exemplo de requisição:**
```json
{
  "data": "2025-11-15"
}
```

## 9. 📈 Monitoramento em Produção
- **Ferramentas utilizadas:**
    Métricas de uso via Hugging Face Analytics
- **Monitoramento manual:**
  - Logs de requisição
  - Comparação entre previsões e valores reais (offline)

## 10. 📚 Documentação Técnica
- **README.md** inclui:
  - Descrição do projeto
  - Instruções de instalação local
  - Como usar a API
  - Link para o deploy no Hugging Face
- **Comentários no código** explicando cada etapa

## 11. 🚀 Deploy
- **Plataforma:** Hugging Face Spaces
- **Link da API:** [https://huggingface.co/spaces/lucivando/docker](https://huggingface.co/spaces/lucivando/docker)
- **Repositório GitHub:** [https://github.com/Overl89/ML_Previsao_Vale](https://github.com/Overl89/ML_Previsao_Vale)
- **Vídeo explicativo:** [https://youtu.be/HuhzEy_bmQA](https://youtu.be/HuhzEy_bmQA)

Endpoints

/fechamento (POST e GET)

POST: Recebe um JSON com a data para previsão.

{ "date": "2025-11-20" }

GET: Permite consulta via parâmetro na URL.

https://lucivando-docker.hf.space/fechamento?date=2025-11-20

Respostas da API

Para datas futuras (previsão):

{ "date": "2025-11-20", "mode": "predict", "yhat": 72.45, "yhat_lower": 70.12, "yhat_upper": 74.88 }

Para datas históricas (dados reais):

{ "date": "2023-11-20", "mode": "historic", "close": 68.32 }

Modelo

Utiliza a biblioteca Prophet do Facebook para previsão de séries temporais.

Treinado com dados históricos de fechamento da ação VALE3.

Arquivo do modelo salvo: modelo_prophet.pkl

Dados históricos: precos_Vale.csv

Estrutura do Projeto

├── app.py # Código da API Flask ├── Dockerfile # Configuração do container Docker ├── requirements.txt # Dependências Python ├── modelo_prophet.pkl # Modelo treinado salvo ├── precos_Vale.csv # Dados históricos de fechamento └── README.md # Documentação do projeto └── BaixaDados.py # Baixa os dados utilizando o yfinance └── TreinaModelo.py # Treina e serializa o modelo └── TestaAPI.py # Testa o endpoint da API após o deploy

Docker

A API roda na porta 7860, conforme exigido pelo Hugging Face Spaces.

Dockerfile:

FROM python:3.9-slim WORKDIR /app COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY . . EXPOSE 7860 CMD ["python", "app.py"]

Docker Hub

Comando para efetuar o pull da imagem: docker push luciusbr89/mlmage:latest

Para baixar os dados da bolsa utilize o arquivo: baixardados.py

Para treinar o modelo com os dados baixados utilize o arquivo: treinamodelo.py

Para testar o endpoint: testaAPI.py

O arquivo app.py usa o fastapi para gerar as previsóes do modelo via api.
