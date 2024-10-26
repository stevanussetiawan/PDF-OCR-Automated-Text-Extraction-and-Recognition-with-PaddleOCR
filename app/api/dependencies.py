from app.services.pdf_ocr_service import PDFOCRService

def pdf_reader_dependency():
    return PDFOCRService()