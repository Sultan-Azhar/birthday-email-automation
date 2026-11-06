from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL_NAME

def load_embeddings() -> HuggingFaceEmbeddings:
    """Hugging Face embedding model load karta hai."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
