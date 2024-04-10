import base64
import json
import numpy as np
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes
from PIL import Image


class ReadPDF:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def pdf_to_base64(self, file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")
        return pdf_base64
    
    def get_pdf_content(self, pdf, poppler_path):
        if pdf.split(".")[-1] in ['pdf', 'PDF']:
            pdf_b64 = self.pdf_to_base64(pdf_file)
            pdf_content = base64.b64decode(pdf_b64)
            images = convert_from_bytes(pdf_content, poppler_path=poppler_path)
        else:
            pdf_content = base64.b64decode(pdf)
            images = convert_from_bytes(pdf_content, poppler_path=poppler_path)        
        return images
    
    def pdf_to_images(self, pdf_file, poppler_path=r"poppler-23.11.0\Library\bin"):
        self.list_img_array = []
        images = self.get_pdf_content(pdf_file, poppler_path)
        for i, image in enumerate(images):
            img_array = np.array(image)
            self.list_img_array.append(img_array)
            
    def get_text(self, res_ocr):
        txt = ""
        if res_ocr:
            for r in res_ocr[0]:
                text_ocr, conf = r[1]
                txt += text_ocr + "\n"
        return txt

    def ocr_pdf(self):
        final_res = {}
        for idx, img_array in enumerate(self.list_img_array):
            res_ocr = self.ocr.ocr(img_array)
            txt = self.get_text(res_ocr)
            # final_res += f"--------------------------------- PAGE {idx+1} ---------------------------------\n"
            final_res.setdefault(f"page_{idx+1}", txt)
        return final_res
            
if __name__ == "__main__":
    # NAMA_FILE = r"test\Surat.pdf"

    with open("test.json", 'r') as f:
        read_json = json.loads(f.read())


    read_pdf = ReadPDF()
    read_pdf.pdf_to_images(read_json["base64"])
    ocr_read_pdf = read_pdf.ocr_pdf()
    print(ocr_read_pdf)
    
        