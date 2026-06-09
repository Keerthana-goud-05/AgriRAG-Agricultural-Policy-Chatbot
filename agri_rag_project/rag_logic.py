from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

VECTOR_STORE_PATH = "vector_store"

def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=VECTOR_STORE_PATH, embedding_function=embeddings)
    return db

def rules_engine(income, land):
    flags = []
    if income < 200000 and land <= 2:
        flags.append("Eligible for PM-Kisan (small/marginal farmer)")
    if income < 60000:
        flags.append("May qualify for PM-KMY pension scheme")
    if land > 0:
        flags.append("Eligible to apply for PMFBY crop insurance")
    return flags

def get_answer(query, income=None, land=None):
    db = load_vector_db()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    result = qa({"query": query})
    answer = result["result"]
    sources = result["source_documents"]

    citations = []
    for doc in sources:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "?")
        citations.append(f"{source} (page {page})")

    rule_tips = []
    if income is not None and land is not None:
        rule_tips = rules_engine(income, land)

    return answer, citations, rule_tips