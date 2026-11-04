from pydantic import BaseModel, Field, field_validator

class SentimentResult(BaseModel):
    label: str
    confidence: float


class AnalyzeResponse(BaseModel):
    summary: str
    sentiment: SentimentResult

class AnalyzeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=20,
        max_length=5000,
        description="Texto longo para análise de sentimento e sumarização"
    )

    @field_validator("text")
    @classmethod
    def validate_text_length(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("O texto não pode estar vazio ou conter apenas espaços em branco.")
        return v