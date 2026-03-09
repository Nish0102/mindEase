from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Custom prompt so Gemini responds like a mental health assistant
PROMPT_TEMPLATE = """
You are MindEase, a compassionate mental health support assistant.
Use the following context from verified mental health resources to answer the user's question.
Always be empathetic, non-judgmental, and supportive.
If you don't know the answer from the context, say "I'm not sure, but I'm here to listen."
Never give medical diagnoses.

Context:
{context}

User: {question}

MindEase:"""

def build_rag_chain(vectorstore, api_key: str):
    """Build the RAG chain using vectorstore and Gemini"""

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        temperature=0.3  # low = more consistent, less random
    )

    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True  # shows which chunks were used
    )

    return chain


def get_response(chain, question: str) -> dict:
    """Get answer from RAG chain"""
    result = chain({"query": question})
    return {
        "answer": result["result"],
        "sources": result["source_documents"]
    }
