from fastapi import FastAPI
from rag_utils import create_rag, ask_question

app=FastAPI()

pdf_path=r"D:\finetune.pdf"

retriever=create_rag(pdf_path)



@app.get("/")
def home():
    return{"message":"RAG is running"}

@app.post("/ask")
def ask(question: str):
    answer=ask_question(question,retriever)

    return {
        "answer":answer
    }