from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest, ChatResponse, IngestResponse
from app.services.chat_service import generate_dummy_answer

app = FastAPI(title="RAG App Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_dummy_answer(request.message)
    return ChatResponse(answer=answer)


@app.post("/api/ingest", response_model=IngestResponse)
def ingest():
    return IngestResponse(
        status="success",
        detail="Ingest endpoint is ready, but ingestion is not implemented yet."
    )