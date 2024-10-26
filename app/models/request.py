from pydantic import BaseModel, Field

class Item(BaseModel):
    base64: str = Field(..., description="Base64 encoded PDF file")