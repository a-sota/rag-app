from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import QuestionRequest, QuestionResponse
from app.rag import build_query_engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

query_engine = build_query_engine()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    response = query_engine.query(request.question)
    return QuestionResponse(answer=str(response))