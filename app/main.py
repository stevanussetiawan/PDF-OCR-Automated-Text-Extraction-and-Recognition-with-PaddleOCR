from fastapi import FastAPI
from app.api.routes import router
from app.core.config import CORS_CONFIG, configure_cors

app = FastAPI(
    title="Optical Character Recognition for PDF File",
    description="An API for performing OCR on PDF files.",
    version="1.0.0"
)

configure_cors(app, CORS_CONFIG)  # Configure CORS

app.include_router(router)