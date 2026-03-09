from langchain_community.document_loaders import PyPDFLoader

def load_pdf(filepath: str):
    """Load a PDF and return list of documents"""
    try:
        loader = PyPDFLoader(filepath)
        documents = loader.load()
        return documents
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None