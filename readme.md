# LangChain Learning Project

This repository contains the projects I built while learning LangChain fundamentals, document processing, and the basics of Retrieval-Augmented Generation (RAG).

The goal was to understand how documents are loaded, split into chunks, embedded into vectors, stored in a vector database, and retrieved based on user queries.

## What I Built

### 1. PDF Summarizer

* Load a PDF using PyPDF2
* Extract text from all pages
* Create a LangChain PromptTemplate
* Generate a summary using Gemini
* Translate the summary into Hindi using a second chain

### 2. Document Chunking

* Load PDFs using LangChain's `PyPDFLoader`
* Convert PDFs into Document objects
* Split documents into chunks using `RecursiveCharacterTextSplitter`
* Experiment with chunk size and chunk overlap
* Inspect chunk content and metadata

### 3. Basic RAG Retrieval

* Create embeddings from document chunks using Gemini Embeddings
* Store embeddings in a FAISS vector store
* Accept user queries
* Retrieve the most relevant chunks using similarity search
* Test retrieval quality with different questions

## Tech Stack

* Python
* LangChain
* Gemini API
* FAISS
* PyPDFLoader
* PyPDF2
* python-dotenv

## Learning Journey

```text
PDF
↓
Document Loader
↓
Document Objects
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store
↓
Similarity Search
↓
Relevant Chunks
```

## Installation

```bash
pip install langchain
pip install langchain-community
pip install langchain-google-genai
pip install faiss-cpu
pip install pypdf
pip install PyPDF2
pip install python-dotenv
```

## Environment Variable

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Key Concepts Learned

* Prompt Templates
* LangChain Chains
* Multi-Step Chains
* Document Loaders
* Metadata
* Text Chunking
* Embeddings
* Vector Databases
* FAISS
* Similarity Search
* Basic RAG Pipeline

## Future Improvements

* Connect retrieval results to Gemini for answer generation
* Build a complete PDF Question Answering system
* Add support for multiple documents
* Explore advanced RAG techniques

```
```
