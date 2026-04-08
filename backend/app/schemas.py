from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


class IngestResponse(BaseModel):
    status: str
    detail: str