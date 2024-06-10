import base64
import json
import numpy as np
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes


class PDFReader:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        self.images = []

    def pdf_file_to_base64(self, file_path):
        with open(file_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode("utf-8")
    
    def decode_base64_pdf(self, base64_pdf):
        return base64.b64decode(base64_pdf)
    
    def convert_pdf_to_images(self, pdf_content, poppler_path):
        return convert_from_bytes(pdf_content, poppler_path=poppler_path)

    def load_pdf(self, pdf_input, poppler_path=r"poppler-23.11.0\Library\bin"):
        if pdf_input.split(".")[-1] in ['pdf', 'PDF']:
            pdf_base64 = self.pdf_file_to_base64(pdf_input)
        else:
            pdf_base64 = pdf_input
            
        print(pdf_base64)
        
        pdf_content = self.decode_base64_pdf(pdf_base64)
        self.images = self.convert_pdf_to_images(pdf_content, poppler_path)
    
    def extract_text_from_ocr(self, ocr_result):
        return "\n".join([line[1][0] for line in ocr_result[0]])

    def ocr_pdf_images(self):
        ocr_results = {}
        for idx, image in enumerate(self.images):
            img_array = np.array(image)
            ocr_result = self.ocr.ocr(img_array)
            ocr_text = self.extract_text_from_ocr(ocr_result)
            ocr_results[f"page_{idx + 1}"] = ocr_text
        return ocr_results


if __name__ == "__main__":
    with open("test.json", 'r') as f:
        input_data = json.load(f)

    pdf_reader = PDFReader()
    pdf_reader.load_pdf(input_data["base64"])
    extracted_text = pdf_reader.ocr_pdf_images()
    print(extracted_text)