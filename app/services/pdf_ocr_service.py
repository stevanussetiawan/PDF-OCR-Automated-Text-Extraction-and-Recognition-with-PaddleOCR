from app.utils.func_pdf_reader import PDFReader

class PDFOCRService:
    def __init__(self):
        self.pdf_reader = PDFReader()

    def main(self, base64_pdf: str):
        self.pdf_reader.load_pdf(base64_pdf)
        return self.pdf_reader.ocr_pdf_images()