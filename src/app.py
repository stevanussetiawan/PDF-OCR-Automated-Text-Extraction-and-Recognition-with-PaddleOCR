from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pdf_ocr_reader import PDFReader
from starlette.responses import JSONResponse

# Pydantic model for request body validation
class Item(BaseModel):
    base64: str = Field(..., description="Base64 encoded PDF file")

app = FastAPI(
    title="Optical Character Recognition for PDF File",
    description="An API for performing OCR on PDF files.",
    version="1.0.0"
)

# Adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_api():
    return {
        "validation": "success",
        "message": "Optical Character Recognition for PDF File"
    }

# Dependency injection for PDF reader service
def pdf_reader_dependency():
    return PDFReader()

@app.post("/predictOCRPDF/")
async def predict(
    data: Item, 
    pdf_reader: PDFReader = Depends(pdf_reader_dependency)
):
    res_ai = {}
    try:
        # Load and process the PDF with OCR
        pdf_reader.load_pdf(data.base64)
        ocr_read_pdf = pdf_reader.ocr_pdf_images()
        res_ai["Prediction_AI"] = ocr_read_pdf
        return {
            "Status": True,
            "Msg": "Proses AI berhasil",
            "Result_AI": res_ai
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def validation_json(data):
    if "base64" not in data:
        return False, "Proses Gagal, key base64 tidak ditemukan"
    return True, "Proses AI berhasil"
