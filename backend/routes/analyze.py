from fastapi import APIRouter, UploadFile,HTTPException, Request
from fastapi.responses import FileResponse
from models.pdf_generator import PDFReportGenerator
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
    


@router.post("/analyze/pdf")
async def get_pdf( request: Request):
    try:
        report_data = await request.json() 
        generator = PDFReportGenerator()
        pdf_path = generator.generate(report_data=report_data)
        return FileResponse(pdf_path, media_type="application/pdf", filename=os.path.basename(pdf_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {str(e)}")
