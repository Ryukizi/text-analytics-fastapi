from app.core.exceptions import ModelInferenceError
from app.ml.sumarization import summarizer
from app.ml.sentiment import analyze_sentiment

def process_text_analysis(text: str) -> dict:
    try:
        summary = summarizer(text)
        sentiment = analyze_sentiment(text)
        return {
            "summary": summary,
            "sentiment": sentiment
        }
    except ValueError as e:
        raise ModelInferenceError(f"Erro nos parâmetros de entrada do modelo: {str(e)}")
    except Exception as e:
        raise ModelInferenceError(f"Falha crítica na inferência do modelo em CPU: {str(e)}")
