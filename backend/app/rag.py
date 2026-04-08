from pathlib import Path
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()

# モデル設定
Settings.llm = OpenAI(model="gpt-5.4-nano")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def build_query_engine():
    documents = SimpleDirectoryReader(input_dir=str(DATA_DIR)).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    return query_engine