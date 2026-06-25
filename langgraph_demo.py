from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from rag_utils import create_rag
from llm_utils import google_chain , tav_search , web_chain

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
    return state

def route(state):
    if state["answer"]=="NOT_FOUND":
        print("Question is out of context....\nAnswer from web results:")
        return "web"
    return "done"


def web_search_node(state):
    web_context=tav_search(
        state['question']
    )
    return {
        "web_context":web_context
    }

def web_generate_node(state):
    chain=web_chain()

    response=chain.invoke({
        "context":state["web_context"],
        "question":state["question"]
    })
    return{
        "answer":response.content
    }



graph= StateGraph(State)

graph.add_node("node1",retriever_node)
graph.add_node("node2",generate_node)
graph.add_node("node3",check_node)
graph.add_node("node4",web_search_node)
graph.add_node("node5",web_generate_node)


graph.add_conditional_edges(
    "node3",
    route,
    {
        "web":"node4",
        "done":END
    }
)

graph.add_edge(START,"node1")
graph.add_edge("node1","node2")
graph.add_edge("node2","node3")
graph.add_edge("node4","node5")
graph.add_edge("node5",END)

app = graph.compile()

while True:
    question=input("User:")
    
    if question.lower()=="exit":
        break

    result=app.invoke({
        "question":question,
        "context":"",
        "answer":"",
        "web_context":""
    })
    print("\nAgent:",result["answer"])
    print()

#for debuging and understanding purpose
""""
for event in app.stream({
    "question":"Who won IPL 2020?",
    "context":"",
    "answer":""
}):
    print(event)
"""