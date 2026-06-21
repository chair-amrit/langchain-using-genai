from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from rag_utils import create_rag

pdf_path=r"D:\finetune.pdf"

retriever=create_rag(pdf_path)

#LangGraph needs to know what data exists in the state.
class State(TypedDict):
    question: str
    context: str
    answer: str

def retriever_node(state):
    docs=retriever.invoke(
        state["question"]
    )
    context="/n/n".join(
        doc.page_content
        for doc in docs
    )
    return {
        "context": context
    }

graph= StateGraph(State)

graph.add_node("node1",retriever_node)

graph.add_edge(START,"node1")
graph.add_edge("node1",END)

app = graph.compile()

for event in app.stream({
    "question":"What is LoRA?",
    "context":"",
    "answer":""
}):
    print(event)