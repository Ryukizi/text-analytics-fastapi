from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_analyze_endpoint_valid():
    payload = {"text": "Estou muito feliz com o resultado deste projeto, funcionou perfeitamente!"}
    response = client.post("/analyze", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "sentiment" in data
    
    sentiment = data["sentiment"]
    assert isinstance(sentiment, dict)
    assert "label" in sentiment
    assert "confidence" in sentiment
    assert sentiment["label"].lower() in ["positivo", "neutro", "negativo"]

def test_analyze_endpoint_invalid():
    payload = {"text": ""}
    response = client.post("/analyze", json=payload)

    assert response.status_code == 422  
    data = response.json()
    assert "detail" in data