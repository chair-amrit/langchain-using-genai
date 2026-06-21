## LangGraph Learning Progress

This project was extended to learn LangGraph and understand how agent workflows differ from traditional LangChain chains.

### What I Learned

* State management using `TypedDict`
* Creating and connecting graph nodes
* Using `START` and `END` nodes
* Executing graphs with `.invoke()` and `.stream()`
* Passing and updating state between nodes
* Conditional routing with `add_conditional_edges()`
* Building decision-based workflows instead of fixed chains

### LangGraph Experiments

#### Basic Graph

Built a simple 2-node graph that receives text and converts it to uppercase.

#### State Tracking

Created a state containing:

* question
* answer
* steps_taken

Passed the state through multiple nodes and observed updates using `.stream()`.

#### Conditional Routing

Implemented a routing function that directs execution to different nodes based on question length using conditional edges.

#### RAG Workflow as a Graph

Converted the document Q&A pipeline into a LangGraph workflow:

```text
retrieve_node
↓
generate_node
↓
check_node
```

* `retrieve_node` retrieves relevant document chunks
* `generate_node` generates an answer using Gemini
* `check_node` validates workflow completion

### Key Takeaway

LangChain chains execute in a fixed sequence, while LangGraph allows stateful workflows, conditional routing, and agent-style execution with decision making and future support for loops and retries.
