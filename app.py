from flask import Flask, request, jsonify
import pandas as pd
import joblib
from datetime import datetime
import os



MODEL_PATH = "artefatos/modelo_prophet.pkl"
CSV_PATH = "artefatos/precos_Vale.csv"  # usado apenas para consultar valores reais quando disponíveis



app = Flask(__name__)

# Carregar modelo e dados no start-up
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}")
modelo = joblib.load(MODEL_PATH)


try:
    df_real = pd.read_csv(CSV_PATH, parse_dates=["Date"])
    df_real = df_real.rename(columns={"Date": "ds", "Close": "y"}).set_index("ds")
except Exception:
    df_real = None


def parse_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception:
        return None


@app.route("/fechamento", methods=["GET", "POST"])
def fechamento():
    # aceitar query param ?date=YYYY-MM-DD ou JSON {"date": "YYYY-MM-DD"}
    if request.method == "GET":
        date_str = request.args.get("date")
    else:
        data = request.get_json(silent=True) or {}
        date_str = data.get("date") or request.args.get("date")

    if not date_str:
        return jsonify({"error": "Parâmetro 'date' é obrigatório (formato YYYY-MM-DD)."}), 400

    d = parse_date(date_str)
    if d is None:
        return jsonify({"error": "Formato de data inválido. Use YYYY-MM-DD."}), 400

    ds = pd.to_datetime(d)

    # Se tivermos dados históricos carregados, checar se existe fechamento real
    if df_real is not None and ds in df_real.index:
        valor_real = float(df_real.loc[ds, "y"])
        return jsonify({
            "date": ds.strftime("%Y-%m-%d"),
            "mode": "historic",
            "close": round(valor_real, 4)
        })

    # Caso contrário, gerar uma previsão com o modelo
    futuro = pd.DataFrame({"ds": [ds]})
    try:
        pred = modelo.predict(futuro).iloc[0]
    except Exception as e:
        return jsonify({"error": "Erro ao gerar previsão: " + str(e)}), 500

    yhat = float(pred["yhat"])
    yhat_lower = float(pred.get("yhat_lower", None)) if "yhat_lower" in pred else None
    yhat_upper = float(pred.get("yhat_upper", None)) if "yhat_upper" in pred else None

    return jsonify({
        "date": ds.strftime("%Y-%m-%d"),
        "mode": "predict",
        "yhat": round(yhat, 4),
        "yhat_lower": round(yhat_lower, 4) if yhat_lower is not None else None,
        "yhat_upper": round(yhat_upper, 4) if yhat_upper is not None else None
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

