import pytest 
from pydantic import ValidationError
from app.schemas.text_schemas import AnalyzeRequest

def test_analyze_request_valid():
    requset_data = AnalyzeRequest(text="Este é um texto de teste válido para análise de sentimento e sumarização.")
    assert requset_data.text == "Este é um texto de teste válido para análise de sentimento e sumarização."

def test_analyze_request_invalid():
    with pytest.raises(ValidationError):
        AnalyzeRequest(text="")
