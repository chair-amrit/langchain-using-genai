from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from rag_utils import create_rag
from llm_utils import google_chain , tav_search

pdf_path=r"D:\finetune.pdf"

retriever=create_rag(pdf_path)

#LangGraph needs to know what data exists in the state.
class State(TypedDict):
    question: str
    context: str
    answer: str
    web_context: str

def retriever_node(state):
    docs=retriever.invoke(
        state["question"]
    )
    context="\n\n".join(
        doc.page_content
        for doc in docs
    )
    return {
        "context": context
    }

def generate_node(state):
    chain=google_chain()
    response=chain.invoke({
        "context": state["context"],
        "question": state["question"]
    })
    return {
        "answer":response.content
    }

def check_node(state):
    if state["answer"]:
        print("Answer generated succesfully")
    return state

def web_node(state):
    web_context=tav_search(
        state['question']
    )
    return {
        "web_context":web_context
    }


graph= StateGraph(State)

graph.add_node("node1",retriever_node)
graph.add_node("node2",generate_node)
graph.add_node("node3",check_node)

graph.add_edge(START,"node1")
graph.add_edge("node1","node2")
graph.add_edge("node2","node3")
graph.add_edge("node3",END)

app = graph.compile()

for event in app.stream({
    "question":"What is LoRA?",
    "context":"",
    "answer":""
}):
    print(event)