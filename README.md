# 🧠 MindEase — RAG-Based Mental Health Support Chatbot

> A safety-aware, mood-adaptive mental health chatbot powered by Retrieval Augmented Generation (RAG), LangChain, and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

---

## 🎯 What Makes This Different

Unlike generic AI chatbots, MindEase:
- Answers from **verified mental health resources** (not hallucinated advice)
- **Detects crisis messages** and shows helplines immediately
- **Shows sources** for every response so users can verify
- **Adapts tone** based on detected mood (sad, neutral, crisis)

---

## 🏗️ Project Structure

```
mindease-rag/
│
├── app.py                  # Main Streamlit UI
├── rag_pipeline.py         # RAG chain builder
├── requirements.txt        # Dependencies
├── .env.example            # API key template
├── .gitignore
│
├── utils/
│   ├── loader.py           # PDF loading
│   ├── chunker.py          # Text splitting
│   ├── embeddings.py       # Vector store creation
│   └── crisis_detector.py  # Mood & crisis detection
│
├── data/                   # Upload PDFs here (gitignored)
└── vectorstore/            # FAISS index stored here (gitignored)
```


## 🚀 Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mindease-rag.git
cd mindease-rag
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key
```bash
cp .env.example .env
# Edit .env and add your key
```
Get your free Gemini API key at: https://makersuite.google.com/app/apikey

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🧪 Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | RAG pipeline orchestration |
| Google Gemini | LLM for generation + embeddings |
| FAISS | Vector similarity search |
| PyPDF2 | PDF document loading |
| Streamlit | Web UI |

---

## 🌟 Features

- [x] PDF upload and indexing
- [x] RAG-powered responses
- [x] Crisis detection with helplines
- [x] Mood detection (SAD / NEUTRAL / CRISIS)
- [x] Source citation for every answer
- [x] Conversation memory within session

---

## ⚠️ Disclaimer

MindEase is not a replacement for professional mental health treatment.
If you are in crisis, please contact a licensed mental health professional.
