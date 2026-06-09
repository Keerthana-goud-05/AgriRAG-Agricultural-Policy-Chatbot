# AgriRAG – AI-Powered Agricultural Policy Chatbot

A RAG (Retrieval-Augmented Generation) chatbot that helps farmers understand government schemes and policies like PM-Kisan, PMFBY, and more.

---

## What It Does

- Reads government policy PDFs and stores them in a local vector database
- Accepts natural language questions from the user
- Retrieves relevant policy chunks and sends them to an LLM
- Returns accurate answers with source citations
- Recommends schemes based on farmer income and land size

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| RAG Framework | LangChain |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB (local) |
| LLM | OpenAI GPT-3.5-turbo |
| PDF Reading | PyPDF |

---

## Project Structure

```
agri_rag_project/
├── app.py                  # Streamlit UI
├── ingest_policies.py      # PDF → ChromaDB pipeline
├── rag_logic.py            # Retrieval + LLM logic
├── requirements.txt        # All dependencies
├── .env                    # API key (do not share)
└── data/
    └── policy_library/     # Put your PDFs here
```

---

## Requirements

- Python 3.10 or higher
- 8 GB RAM minimum
- Internet connection (for OpenAI API)
- An OpenAI API key

---

## Setup and Installation

### 1. Clone or download the project

```
git clone https://github.com/your-username/agri-rag-chatbot.git
cd agri-rag-chatbot
```

### 2. Create a virtual environment

```
python -m venv venv
```

### 3. Activate the virtual environment

Windows:
```
venv\Scripts\activate
```

Mac / Linux:
```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Set your API key

Open the `.env` file and replace the placeholder:

```
OPENAI_API_KEY=your_actual_key_here
```

Get a key at: https://platform.openai.com/api-keys

---

## Running the Project

### Step 1 — Add PDFs

Copy any government policy PDFs into:

```
data/policy_library/
```

Examples: PM-Kisan circular, PMFBY document, loan scheme PDFs.

### Step 2 — Run ingestion (do this once, or when you add new PDFs)

```
python ingest_policies.py
```

This reads all PDFs, splits them into chunks, and saves them to the local vector database.

Expected output:
```
Loading: pmkisan.pdf
Loading: pmfby.pdf
Total chunks created: 142
Vector store saved!
Done! Ready to query.
```

### Step 3 — Launch the chatbot

```
streamlit run app.py
```

Open your browser at: http://localhost:8501

---

## How to Use the App

1. Type your question in the text box
   - Example: *"What is the eligibility for PM-Kisan?"*
2. Click **Ask**
3. The answer appears with source citations below it
4. (Optional) Enter your income and land size in the sidebar and check **Use profile for recommendations** to get personalized scheme suggestions

---

## Example Questions to Try

- What are the benefits of PM-Kisan scheme?
- How do I apply for PMFBY crop insurance?
- What is the income limit for small farmer schemes?
- Which schemes are available for farmers in Maharashtra?

---

## Common Errors and Fixes

| Error | Fix |
|---|---|
| `No PDFs found` | Add PDFs to `data/policy_library/` and re-run ingestion |
| `Invalid API key` | Check your `.env` file has the correct key |
| `No vector store found` | Run `python ingest_policies.py` first |
| `Slow response` | Reduce `chunk_size` in `ingest_policies.py` to 300 |
| `Wrong answers` | Add better quality PDFs to the policy library |

---

## Resetting the Vector Database

If you want to start fresh:

```
rm -rf vector_store/
python ingest_policies.py
```

---

## Future Improvements

- Support for regional languages (Hindi, Telugu, etc.)
- Voice input for farmers with low digital literacy
- Mobile app version
- Offline mode with cached summaries

---

## Team

Built as an academic project by a team of 6 students.

---

## Disclaimer

This chatbot is for informational purposes only. Always verify policy details with official government portals or a local agricultural officer.