from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

#provide pdf path
path=input("Enter the path of the PDF file:").strip().strip('"')

#load pdf
loader = PyPDFLoader(path)
docs=loader.load()

#ask qustion
query=input("Ask a question: ")

#splitter:provide chunk size and overlap
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=90
)

#split into chunks
chunks=splitter.split_documents(docs)

print(f"Total chunks:{len(chunks)}")

#create embeddings
embeds=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

#create FAISS
vectors=FAISS.from_documents(
    chunks,
    embeds
)

#create retirever
retriever=vectors.as_retriever(
    search_kwargs={"k":2}
)

#retrieve chunks
retrieved_docs=retriever.invoke(query)

for i, doc in enumerate(retrieved_docs):
    print(f"===========Retrieved Chunk {i+1}:============")
    print(doc.page_content)

#join the retieved chunks(doc object) into text object for gemini model 
cont="\n\n".join(
    doc.page_content for doc in retrieved_docs
)

#create llm
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

#provide prompt
prompt=ChatPromptTemplate.from_template(
    """
    Answer the question using only the provided context:

    If the answer is not present in the context, reply:
    "I could not find this information in the document."

    Do not use outside knowledge.   

    Context=
    {context}
    
    Qeustion=
    {question}
    
    """
)

#create the chain(prompt->llm)
chain = prompt | llm

#generate answer and get the response
response=chain.invoke({
    "context":cont,
    "question":query
})

#print the answer
print("==========ANSWER==========")
print(response.content)
