from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    message:list[str]

def chat_node(state):
    print("Current memory:")
    print(state["message"])
    return state

graph=StateGraph(State)

graph.add_node("chat",chat_node)

graph.add_edge(START,"chat")
graph.add_edge("chat",END)

memory=MemorySaver()

app=graph.compile(
    checkpointer=memory
)

config={
    "configurable":{
        "thread_id":"chat1"
    }
}

run1=app.invoke(
    {
        "message":[
            "My name is Amrit"
        ]
    },config=config
)

run2=app.invoke(
    {
        "message":[
            "What is my name?"
        ]
    },config=config
)

print(run1)
print(run2)