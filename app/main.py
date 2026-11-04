from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.exceptions import ModelInferenceError
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="API de Análise de Texto",
    description="API modularizada para sumarização e análise de sentimento utilizando FastAPI e Transformers.",
    version="2.0.0"
)

app.include_router(analyze_router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Análise de Texto. Use o endpoint /analyze para enviar textos para análise."}

@app.exception_handler(ModelInferenceError)
async def model_inference_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": exc.message},
    )