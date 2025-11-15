
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

