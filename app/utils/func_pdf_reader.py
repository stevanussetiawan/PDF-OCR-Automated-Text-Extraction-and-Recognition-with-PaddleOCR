import base64
import json
import numpy as np
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes

class PDFReader:
    def __init__(self, poppler_path="app\\poppler-23.11.0\\Library\\bin"):
        # Initialize OCR model and PDF to image conversion path
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        self.poppler_path = poppler_path
        self.images = []
        
    def ocr_pdf_images(self):
        """
        Perform OCR on each page image and return extracted text.
        Returns a dictionary with page numbers as keys and extracted text as values.
        """
        ocr_results = {}
        for idx, image in enumerate(self.images):
            img_array = np.array(image)
            ocr_result = self.ocr.ocr(img_array)
            ocr_text = self._extract_text_from_result(ocr_result)
            ocr_results[f"page_{idx + 1}"] = ocr_text
        return ocr_results

    def _file_to_base64(self, file_path):
        # Convert PDF file at given path to base64 string
        with open(file_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode("utf-8")

    def _decode_base64(self, base64_pdf):
        # Decode base64 string to binary content
        return base64.b64decode(base64_pdf)

    def _convert_pdf_content_to_images(self, pdf_content):
        # Convert binary PDF content to a list of images
        return convert_from_bytes(pdf_content, poppler_path=self.poppler_path)

    def load_pdf(self, pdf_input):
        """
        Loads PDF for OCR processing.
        If `pdf_input` is a file path ending in .pdf, it will be converted to base64.
        Otherwise, it's assumed to be a base64-encoded PDF string.
        """
        # Determine if `pdf_input` is a file path or base64 string
        pdf_base64 = self._file_to_base64(pdf_input) if pdf_input.lower().endswith('.pdf') else pdf_input
        
        # Decode base64 PDF content and convert to images
        pdf_content = self._decode_base64(pdf_base64)
        self.images = self._convert_pdf_content_to_images(pdf_content)

    def _extract_text_from_result(self, ocr_result):
        # Extract and combine text from OCR result
        return "\n".join([line[1][0] for line in ocr_result[0]])

if __name__ == "__main__":
    # Load input data from JSON file
    with open("test.json", 'r') as f:
        input_data = json.load(f)

    # Initialize and use PDFReader to process the PDF
    pdf_reader = PDFReader()
    pdf_reader.load_pdf(input_data["base64"])
    extracted_text = pdf_reader.ocr_pdf_images()
    
    # Output extracted text
    print(extracted_text)