# Document Q&A Agent API

A Retrieval-Augmented Generation (RAG) application built while learning LangChain, vector databases, and AI application deployment with FastAPI.

The project allows users to ask questions about a PDF document through a REST API. The system retrieves relevant document chunks using semantic search and uses Gemini to generate answers grounded in the document content.

## Features

* Load and process PDF documents
* Split documents into chunks
* Generate embeddings using Gemini Embeddings
* Store vectors in FAISS
* Retrieve relevant document chunks
* Generate context-aware answers using Gemini
* FastAPI endpoint for document question answering
* Auto-generated API documentation with Swagger UI

## Architecture

```text
PDF
↓
PyPDFLoader
↓
Document Chunks
↓
Gemini Embeddings
↓
FAISS Vector Store
↓
Retriever
↓
Relevant Context
↓
Gemini 2.5 Flash
↓
Answer
↓
FastAPI Endpoint
↓
JSON Response
```

## Tech Stack

* Python
* LangChain
* Google Gemini API
* FAISS
* FastAPI
* Uvicorn
* PyPDFLoader
* python-dotenv

## API Endpoint

### Ask a Question

```http
POST /ask
```

Example:

```json
{
    "question": "What is LoRA?"
}
```

Response:

```json
{
    "answer": "LoRA is a parameter-efficient fine-tuning technique..."
}
```

## Installation

```bash
pip install langchain
pip install langchain-community
pip install langchain-google-genai
pip install faiss-cpu
pip install fastapi
pip install uvicorn
pip install pypdf
pip install python-dotenv
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Run the API

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

to test the API using the Swagger UI.

## What I Learned

* LangChain fundamentals
* Prompt templates and chains
* Document loaders
* Text chunking and overlap
* Embeddings
* Vector databases
* FAISS similarity search
* Retrievers
* Retrieval-Augmented Generation (RAG)
* FastAPI deployment
* Building AI applications as APIs

## Future Improvements

* Support multiple PDFs
* Chat memory and conversation history
* Persistent vector storage
* Upload PDFs through the API
* Advanced RAG techniques and reranking

## LangGraph Fundamentals

As the next step in my AI engineering learning path, I started learning LangGraph to understand how agent workflows differ from traditional LangChain chains.

### Concepts Learned

* State: Shared data that flows through the graph
* Nodes: Functions that read and modify state
* Edges: Connections that determine execution flow
* START and END nodes
* Graph compilation and execution
* State propagation between nodes

### First LangGraph Project

Built a simple 2-node graph:

```text
START
↓
Node 1
↓
Node 2
↓
END
```

Workflow:

```text
Input: hello world
↓
Node 1
↓
Node 2 (convert text to uppercase)
↓
Output: HELLO WORLD
```

### Key Takeaway

Unlike LangChain chains that execute in a fixed linear sequence, LangGraph introduces graph-based workflows where state can move between nodes, enabling conditional routing, loops, retries, and agent-like behavior.
