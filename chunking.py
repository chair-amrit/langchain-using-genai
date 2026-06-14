from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

path=input("Enter the path of the PDF file:").strip().strip('"')

loader = PyPDFLoader(path)
docs=loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks=splitter.split_documents(docs)

print(f"Total chunks:{len(chunks)}")

for i in range (min(3,len(chunks))):
    print(f"=========={i+1}Chunk==========")
    print(chunks[i].page_content)
    print(chunks[i].metadata)