from fastapi import APIRouter, UploadFile,HTTPException
from models.request_model import AnalyzeRequest
from services.code_review_service import CodeReviewService
import os
import uuid

router = APIRouter()

@router.post("/analyze/json")
async def analyze_code(payload: AnalyzeRequest):
    service = CodeReviewService()

    if payload.code:
        return service.analyze_code(code_text=payload.code, user=payload.user)

    else:
        raise HTTPException(status_code=400, detail="No code provided.")
    
@router.post("/analyze/file")
async def analyze_code(
    file: UploadFile = None,
):
    service = CodeReviewService()

    user = {"id": "user_id", "email": "user_email"}

    if file:
        ext = os.path.splitext(file.filename)[1]
        temp_name = f"upload_{uuid.uuid4()}{ext}"
        temp_path = os.path.join("temp_uploads", temp_name)
        os.makedirs("temp_uploads", exist_ok=True)

        with open(temp_path, "wb") as f:
            f.write(await file.read())

        return service.analyze_code(file_path=temp_path, user=user)

    else:
        raise HTTPException(status_code=400, detail="file provided.")