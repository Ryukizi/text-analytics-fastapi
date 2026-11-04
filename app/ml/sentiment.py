from transformers import pipeline

print("Carregando modelos de análise de sentimento e sumarização...")

sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=-1
)

def analyze_sentiment(text: str) -> dict:
    result = sentiment_analyzer(text)[0]

    label_map = {
        "positive": "Positivo",
        "neutral": "Neutro",
        "negative": "Negativo"
    }

    raw_label = result["label"].lower()
    translated_label = label_map.get(raw_label, "neutro")

    return {
        "label": translated_label,
        "confidence": round(result["score"], 2)
    }