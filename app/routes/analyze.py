from fastapi import APIRouter, HTTPException
from app.schemas.text_schemas import AnalyzeRequest, AnalyzeResponse
from app.services.analysis_service import process_text_analysis

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.post("", response_model=AnalyzeResponse)
def analyze_text(payload: AnalyzeRequest):
    result = process_text_analysis(payload.text)
    return AnalyzeResponse(**result)