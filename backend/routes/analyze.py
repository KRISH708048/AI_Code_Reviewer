from fastapi import APIRouter, HTTPException
from models.request_model import AnalyzeRequest
from services.code_review_service import CodeReviewService

router = APIRouter()

@router.post("/analyze")
async def analyze_code(payload: AnalyzeRequest):
    service = CodeReviewService()

    if payload.code:
        return service.analyze_code(code_text=payload.code, user=payload.user)

    elif payload.file_path:
        return service.analyze_code(file_path=payload.file_path, user=payload.user)

    else:
        raise HTTPException(status_code=400, detail="No code or file_path provided.")
