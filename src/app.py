from fastapi import FastAPI
from pydantic import BaseModel
from pdf_ocr_reader import PDFReader

# Define a Pydantic model for request body validation
class Item(BaseModel):
    base64: str

app = FastAPI()
@app.get("/")
def get_api():
    sts = "success"
    msg = "Optical Character Recognition for PDF File"
    res_message = {}
    res_message.setdefault("validation", sts)
    res_message.setdefault("message",msg)
    return res_message

@app.post("/predictOCRPDF/")
def predict(data: dict):
    read_pdf = PDFReader()
    res_ai = {}
    sts = False
    try:
        sts, msg = validation_json(data)        
        if sts:
            b64_pdf = data["base64"]
            read_pdf = PDFReader()
            read_pdf.load_pdf(b64_pdf)
            ocr_read_pdf = read_pdf.ocr_pdf_images()  
            res_ai.setdefault("Prediction_AI", f"{ocr_read_pdf}")
            
    except Exception as e:
        msg = e

    resp = {}
    resp.setdefault("Status", sts)
    resp.setdefault("Msg", msg)
    resp.setdefault("Result_AI", res_ai) 
    return resp

def validation_json(data):
    sts = True
    msg = "Proses AI berhasil"
    if "base64" not in data:
        sts = False
        msg = "Proses Gagal, key base64 tidak ditemukan"    
    return sts, msg