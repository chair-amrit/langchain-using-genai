from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from rag_utils import create_rag
from llm_utils import google_chain , tav_search , web_chain , router_chain
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver

pdf_path=r"D:\finetune.pdf"

retriever=create_rag(pdf_path)

#LangGraph needs to know what data exists in the state.
class State(TypedDict):
    question: str
    context: str
    answer: str
    web_context: str
    messages: Annotated[list,add_messages]
    route: str

#check query and determine if chat/valid question/invalid query and update route in state
def router_node(state):
    chain=router_chain()
    response=chain.invoke({
        "query":state["question"]
    })
    return {
        "route": response.content.strip().lower().replace(".", "")
    }

#fuction to return route from state
def route1(state):
    return state["route"]

#if invalid query
def invalid_node(state):
    return{
        "answer":"I couldn't understand that input."
    }

#if normal chatting
def chat_node(state):
    return{
        "answer":"I can answer questions about the document or chat with you."
    }


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
        "messages":state["messages"],
        "context": state["context"],
        "question": state["question"]
    })
    return {
        "answer":response.content
    }

def check_node(state):
    return state

def route2(state):
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

def save_node(state):
    print(state["messages"])
    return {
        "messages":[
            HumanMessage(content=state["question"]),
            AIMessage(content=state["answer"])
        ]
    }

memory=MemorySaver()

config = {
    "configurable":{
        "thread_id":"chat1"
    }
}

graph= StateGraph(State)

graph.add_node("check_query",router_node)
graph.add_node("invalid_node",invalid_node)
graph.add_node("chat_node",chat_node)
graph.add_node("node1",retriever_node)
graph.add_node("node2",generate_node)
graph.add_node("node3",check_node)
graph.add_node("node4",web_search_node)
graph.add_node("node5",web_generate_node)
graph.add_node("save",save_node)

#check query and redirect to appropriate node
graph.add_conditional_edges(
    "check_query",
    route1,
    {
        "chat":"chat_node",
        "nonsense":"invalid_node",
        "doc":"node1"
    }
)
graph.add_conditional_edges(
    "node3",
    route2,
    {
        "web":"node4",
        "done":"save"
    }
)

graph.add_edge(START,"check_query")
graph.add_edge("node1","node2")
graph.add_edge("node2","node3")
graph.add_edge("node4","node5")
graph.add_edge("node5","save")
graph.add_edge("save",END)
graph.add_edge("invalid_node",END)
graph.add_edge("chat_node",END)


app = graph.compile(
    checkpointer=memory
)

while True:
    question=input("User:")
    
    if question.lower()=="exit":
        break

    result=app.invoke({
        "question":question,
        "context":"",
        "answer":"",
        "web_context":"",
        "messages":[],
        "route":""
    },config=config
    )
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