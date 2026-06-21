from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#LangGraph needs to know what data exists in the state.
class State(TypedDict):
    question:str

#check length
def check_length(state):
    return state

#short node
def short_node(state):
    print("Short Question")
    return state

#complete update steps taken
def long_node(state):
    print("Long Question")
    return state

#condotional node function
def route(state):
    if len(state['question'])<5:
        return "short"
    else:
        return "long"
    
#create graqh
graph = StateGraph(State)

#addnodes
graph.add_node("check_length",check_length)
graph.add_node("short_node",short_node)
graph.add_node("long_node",long_node)

#connect nodes by edges
graph.add_edge(START,"check_length")

#conditional edge
graph.add_conditional_edges(
    "check_length",
    route,
    {
        "short":"short_node",
        "long":"long_node"
    }
)

graph.add_edge("short_node",END)
graph.add_edge("long_node",END)

#Convert flowchart into executable program
app=graph.compile()

#use .stream
for event in app.stream({
    "question":"Hi"
}):
    print(event)