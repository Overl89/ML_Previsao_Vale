Documentação do Projeto: Previsão de Ações com Flask e Prophet

Este projeto consiste em uma API desenvolvida em Flask que utiliza o modelo Prophet para realizar previsões de fechamento das ações da Vale (VALE3). A API está containerizada com Docker e hospedada no Hugging Face Spaces, permitindo acesso via HTTP para consultas de previsão.

Endpoints

/fechamento (POST e GET)

POST: Recebe um JSON com a data para previsão.

{
  "date": "2025-11-20"
}

GET: Permite consulta via parâmetro na URL.

https://lucivando-docker.hf.space/fechamento?date=2025-11-20

Respostas da API

Para datas futuras (previsão):

{
  "date": "2025-11-20",
  "mode": "predict",
  "yhat": 72.45,
  "yhat_lower": 70.12,
  "yhat_upper": 74.88
}

Para datas históricas (dados reais):

{
  "date": "2023-11-20",
  "mode": "historic",
  "close": 68.32
}

Modelo

Utiliza a biblioteca Prophet do Facebook para previsão de séries temporais.

Treinado com dados históricos de fechamento da ação VALE3.

Arquivo do modelo salvo: modelo_prophet.pkl

Dados históricos: precos_Vale.csv

Estrutura do Projeto

├── app.py                 # Código da API Flask
├── Dockerfile             # Configuração do container Docker
├── requirements.txt       # Dependências Python
├── modelo_prophet.pkl     # Modelo treinado salvo
├── precos_Vale.csv        # Dados históricos de fechamento
└── README.md              # Documentação do projeto
└── BaixaDados.py          # Baixa os dados utilizando o yfinance
└── TreinaModelo.py        # Treina e serializa o modelo
└── TestaAPI.py            # Testa o endpoint da API após o deploy

Docker

A API roda na porta 7860, conforme exigido pelo Hugging Face Spaces.

Dockerfile:

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]

Docker Hub

Comando para efetuar o pull da imagem:
docker push luciusbr89/mlmage:latest

Para baixar os dados da bolsa utilize o arquivo: baixardados.py

Para treinar o modelo com os dados baixados utilize o arquivo: treinamodelo.py

Para testar o endpoint: testaAPI.py

O arquivo app.py usa o fastapi para gerar as previsóes do modelo via api.
