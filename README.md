## Overview
The paddleocr-pdf-ocr repository hosts a project aimed at automating text extraction and recognition from PDF documents using PaddleOCR, a powerful OCR (Optical Character Recognition) tool based on deep learning techniques.

## Project Structure

```
app/
├── main.py                    # Entry point
├── api/                       
│   ├── routes.py              # API route definitions
│   └── dependencies.py        # Dependency functions
├── core/
│   └── config.py              # Configuration settings (e.g., CORS settings)
├── models/
│   └── request.py             # Pydantic models for request validation
├── services/
│   └── pdf_ocr_service.py     # PDF OCR logic using PDFReader
└── utils/
    └── func_pdf_reader.py     # Main Function of pdf reader
```

## API Usage
Send a POST request to /predictOCRPDF with a JSON body containing the Instagram comment to be analyzed:

```JSON
{
	"filename": str,
	"base64": str
}
```

The API will return the OCR result:

```JSON
{
	"Status": bool,
	"Msg": str,
	"Result_AI": {
		"Prediction_AI": dict,
	}
}
```
Example:

![Alt text](images/Capture.JPG)





