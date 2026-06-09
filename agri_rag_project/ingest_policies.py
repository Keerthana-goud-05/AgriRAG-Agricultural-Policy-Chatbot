import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PDF_FOLDER = "data/policy_library"
VECTOR_STORE_PATH = "vector_store"

def load_pdfs(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            print(f"Loading: {filename}")
            loader = PyPDFLoader(path)
            docs.extend(loader.load())
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")
    return chunks

def store_embeddings(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=VECTOR_STORE_PATH)
    db.persist()
    print("Vector store saved!")

if __name__ == "__main__":
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)
        print(f"Created folder: {PDF_FOLDER}")
        print("Please put your policy PDFs in that folder and run again.")
    else:
        docs = load_pdfs(PDF_FOLDER)
        if not docs:
            print("No PDFs found. Add PDFs to data/policy_library/")
        else:
            chunks = split_docs(docs)
            store_embeddings(chunks)
            print("Done! Ready to query.")