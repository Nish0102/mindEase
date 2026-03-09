import streamlit as st
import os
from dotenv import load_dotenv
from utils.loader import load_pdf
from utils.chunker import chunk_documents
from utils.embeddings import create_vectorstore
from utils.crisis_detector import detect_mood, HELPLINE
from rag_pipeline import build_rag_chain, get_response

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(page_title="MindEase", page_icon="🧠")
st.title("🧠 MindEase — Mental Health Support Chatbot")
st.caption("Powered by RAG + Google Gemini | Built by Nishanth")

# ─── Session State (memory) ────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state:
    st.session_state.chain = None

# ─── Sidebar: PDF Upload ───────────────────────────────────
with st.sidebar:
    st.header("📄 Upload Resources")
    uploaded_file = st.file_uploader("Upload mental health PDF", type="pdf")

    if uploaded_file and st.button("Process PDF"):
        with st.spinner("Reading and indexing PDF..."):
            # Save uploaded file temporarily
            with open("data/temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            # RAG Pipeline
            docs = load_pdf("data/temp.pdf")
            chunks = chunk_documents(docs)
            vectorstore = create_vectorstore(chunks, API_KEY)
            st.session_state.chain = build_rag_chain(vectorstore, API_KEY)
            st.success(f"✅ Indexed {len(chunks)} chunks!")

# ─── Chat Interface ────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("How are you feeling today?"):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Detect mood
    mood = detect_mood(user_input)

    with st.chat_message("assistant"):
        if mood == "CRISIS":
            # Show helpline immediately
            st.error("I'm concerned about you. Please reach out for help:")
            st.markdown(HELPLINE)
            response = "You're not alone. Please contact a crisis helpline immediately."

        elif st.session_state.chain is None:
            response = "Please upload a mental health PDF first so I can give you informed support 💙"
            st.markdown(response)

        else:
            with st.spinner("Thinking..."):
                result = get_response(st.session_state.chain, user_input)
                response = result["answer"]

                # Show mood indicator
                if mood == "SAD":
                    st.info("💙 I can sense you're going through something difficult.")

                st.markdown(response)

                # Show sources
                with st.expander("📚 Sources used"):
                    for doc in result["sources"]:
                        st.caption(doc.page_content[:200] + "...")

    st.session_state.messages.append({"role": "assistant", "content": response})
