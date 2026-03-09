from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, api_key: str):
    """Convert chunks to vectors and store in FAISS"""
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def load_vectorstore(path: str, api_key: str):
    """Load existing vectorstore from disk"""
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    vectorstore = FAISS.load_local(path, embeddings)
    return vectorstore