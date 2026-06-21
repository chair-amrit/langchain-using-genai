from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#LangGraph needs to know what data exists in the state.
class State(TypedDict):
    question:str
    answer:str
    steps_taken:list


#Add question
def node1(State):
    return {
        "steps_taken":State["steps_taken"]+["question_received"]
    }

#add answer update steps taken
def node2(State):
    return {
        "answer":f"Answer for {State['question']}",
        "steps_taken":State["steps_taken"]+["answer_generated"]
    }

#complete update steps taken
def node3(State):
    return {
        "steps_taken" : State["steps_taken"]+["completed"]
    }

#create graqh
graph = StateGraph(State)

#addnodes
graph.add_node("node1",node1)
graph.add_node("node2",node2)
graph.add_node("node3",node3)

#connect nodes
graph.add_edge(START,"node1")
graph.add_edge("node1","node2")
graph.add_edge("node2","node3")
graph.add_edge("node3",END)

#Convert flowchart into executable program
app=graph.compile()

#use .stream
for event in app.stream({
    "question":"What is LoRA?",
    "answer":"",
    "steps_taken":[]
}):
    print(event)