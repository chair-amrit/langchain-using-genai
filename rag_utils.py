from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def create_rag(pdf_path):
    #load pdf
    loader = PyPDFLoader(pdf_path)
    docs=loader.load()

    #splitter:provide chunk size and overlap
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=90
    )

    #split into chunks
    chunks=splitter.split_documents(docs)

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

    return retriever

def ask_question(query,retriever):
    #retrieve chunks
    retrieved_docs=retriever.invoke(query)

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
    
        Question=
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

    return response.content