from datetime import datetime
from pydantic import BaseModel, ConfigDict


class DocumentItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    file_name: str
    content_type: str
    created_at: datetime


class AskRequest(BaseModel):
    question: str
    document_id: int | None = None


class AskResponse(BaseModel):
    document_id: int
    question: str
    answer: str


class UploadResponse(BaseModel):
    message: str
    document_id: int
    chunks_created: int
