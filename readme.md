# Conversational Adaptive RAG Agent

A conversational Retrieval-Augmented Generation (RAG) system built with LangGraph. The agent intelligently routes user requests, rewrites follow-up questions, retrieves relevant document context, optionally searches the web with user permission, and maintains conversation memory.

## Features

- Intent Router
  - Classifies input into:
    - Chat
    - Document Question
    - Invalid Input

- Conversational Memory
  - Stores previous user and assistant messages using LangGraph MemorySaver.

- Question Rewriting
  - Converts follow-up questions into standalone questions before retrieval.

- PDF RAG
  - Retrieves relevant chunks using FAISS embeddings.

- Web Search Fallback
  - If the document cannot answer the query, the user is asked whether to search the web.
  - Uses Tavily search.

- Modular LangGraph Workflow
  - Each task is implemented as an independent node.

## Workflow

User Query
↓
Router
├── Chat
├── Invalid
└── Document Question
        ↓
Question Rewriter
        ↓
Retriever
        ↓
Gemini Answer Generation
        ↓
Answer Found?
├── Yes → Save Memory → Response
└── No
      ↓
Ask User Permission
      ↓
Yes → Web Search → Generate Answer → Save Memory
No  → End

## Tech Stack

- LangGraph
- LangChain
- Google Gemini
- Groq (Llama 3.1 8B Instant)
- FAISS
- HuggingFace Embeddings
- Tavily Search API
- Python

## Models

| Task | Model |
|------|-------|
| Router | Llama 3.1 8B Instant (Groq) |
| Question Rewriter | Llama 3.1 8B Instant (Groq) |
| Final Answer | Gemini |

## Current Limitations

- FAISS is in-memory (not persistent).
- Retrieval quality is determined by the LLM instead of a dedicated grader.
- Chat mode is currently a placeholder.

## Planned Improvements

- Chroma Vector Database
- Retrieval Grader
- Real Chat Agent
- Source Citations
- Multi-Agent Architecture