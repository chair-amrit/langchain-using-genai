from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

path=input("Enter the path of the PDF file:").strip().strip('"')

loader = PyPDFLoader(path)
docs=loader.load()

query=input("Ask a question: ")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=90
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

retriever=vectors.as_retriever(
    search_kwargs={"k":2}
)

docs=retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"===========Retrieved Chunk {i+1}:============")
    print(doc.page_content)

cont="\n\n".join(
    doc.page_content for doc in docs
)

print(cont)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt=ChatPromptTemplate.from_template(
    """
    Answer the question using only the provided context:

    Context=
    {context}
    
    Qeustion=
    {question}
    
    """
)

chain = prompt | llm

response=chain.invoke({
    "context":cont,
    "question":query
})

print("==========ANSWER==========")
print(response.content)
