from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

PROMPT_TEMPLATE="""You are MindEase, a compassionate mental health support assistant.
Use the following context from verified mental health resources to answer the user question.
Always be empathetic, non-judgmental and supportive.
If you dont know the answer say I am not sure but I am here to listen.
Never give medical diagnoses.

Context:
{context}

User: {question}

MindEase:"""

def build_rag_chain(vectorstore,api_key):
    llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=api_key,temperature=0.3)
    prompt=PromptTemplate(template=PROMPT_TEMPLATE,input_variables=["context","question"])
    chain=RetrievalQA.from_chain_type(llm=llm,retriever=vectorstore.as_retriever(search_kwargs={"k":3}),chain_type_kwargs={"prompt":prompt},return_source_documents=True)
    return chain

def get_response(chain,question):
    result=chain({"query":question})
    return {"answer":result["result"],"sources":result["source_documents"]}
