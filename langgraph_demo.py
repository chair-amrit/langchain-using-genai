from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#LangGraph needs to know what data exists in the state.
class state(TypedDict):
    text:str

#It does nothing just to see how data flow.
def node1(state):
    return state

#This modifies the state.
def node2(state):
    return {
        "text":state["text"].upper()
    }

#create graqh
graph = StateGraph(state)

#addnodes
graph.add_node("node1",node1)
graph.add_node("node2",node2)

#connect nodes
graph.add_edge(START,"node1")
graph.add_edge("node1","node2")
graph.add_edge("node2",END)

#Convert flowchart into executable program
app=graph.compile()

#run
result=app.invoke({
    "text":"hello world"
})

print(result)