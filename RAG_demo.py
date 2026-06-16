from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

path=input("Enter the path of the PDF file:").strip().strip('"')

loader = PyPDFLoader(path)
docs=loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks=splitter.split_documents(docs)

print(f"Total chunks:{len(chunks)}")

embeds=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vectors=FAISS.from_documents(
    chunks,
    embeds
)

query=input("Ask a question: ")

results=vectors.similarity_search(
    query,
    k=2
)

for i, doc in enumerate(results):
    print(f"Match{i+1}")
    print(doc.page_content)