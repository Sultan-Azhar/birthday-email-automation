from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import CHROMA_DIR, COLLECTION_NAME

def create_vector_store(
    chunks: list[Document],
    embeddings: HuggingFaceEmbeddings
) -> Chroma:
    """Chunks ke embeddings persistent ChromaDB mein save karta hai."""
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME
    )
