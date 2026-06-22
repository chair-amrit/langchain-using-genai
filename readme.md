# Hybrid RAG Agent with LangGraph

A document question-answering agent built using LangChain, LangGraph, FAISS, Gemini, and Tavily Search.

The agent first searches an uploaded PDF for relevant information. If the answer is not found in the document, it automatically performs a web search and generates an answer using online sources.

## Features

* PDF document loading with PyPDFLoader
* Document chunking using RecursiveCharacterTextSplitter
* Vector embeddings using Gemini Embeddings
* FAISS vector database for retrieval
* Retrieval-Augmented Generation (RAG)
* LangGraph workflow orchestration
* Conditional routing based on answer availability
* Tavily web search fallback
* Gemini-powered answer generation
* Final answer returned through a single agent workflow

## Workflow

Question
↓
Retrieve Relevant Chunks
↓
Generate Answer from Document
↓
Answer Found?

YES → Return Answer

NO → Search Web (Tavily)
↓
Generate Answer from Web Results
↓
Return Answer

## LangGraph Nodes

* `retriever_node` – Retrieves relevant document chunks
* `generate_node` – Generates answer from document context
* `check_node` – Validates whether an answer was found
* `web_search_node` – Searches the web using Tavily
* `web_generate_node` – Generates answer using web search results

## Technologies Used

* Python
* LangChain
* LangGraph
* Google Gemini
* FAISS
* Tavily Search
* FastAPI
* dotenv

## What I Learned

* RAG pipeline architecture
* Document retrieval using vector databases
* LangGraph state management
* Nodes and edges in graph workflows
* Conditional routing
* Agent decision-making
* Tool integration
* Hybrid RAG + Web Search systems
* Building fallback mechanisms for missing information
* Organizing AI projects into reusable modules

## Future Improvements

* Citation support
* Source attribution
* Multi-tool agents
* Memory integration
* ToolNode implementation
* Multi-document retrieval
* Agent loops and self-correction
