from fastapi import APIRouter, Depends, HTTPException
from app.models.request import Item
from app.api.dependencies import pdf_reader_dependency

router = APIRouter()

@router.get("/")
async def get_api():
    return {
        "validation": "success",
        "message": "Optical Character Recognition for PDF File"
    }

@router.post("/predictOCRPDF/")
async def predict(data: Item, pdf_reader=Depends(pdf_reader_dependency)):
    try:
        ocr_result = pdf_reader.main(data.base64)
        return {
            "Status": True,
            "Msg": "Proses AI berhasil",
            "Result_AI": {"Prediction_AI": ocr_result}
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))