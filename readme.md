# Document Q&A Agent

A simple Retrieval-Augmented Generation (RAG) project built while learning LangChain.

The application allows users to ask questions about any PDF document. Instead of sending the entire document to the LLM, the PDF is split into chunks, embedded into vectors, stored in a FAISS vector database, and the most relevant chunks are retrieved before generating an answer.

## What I Built

* Loaded PDF documents using `PyPDFLoader`
* Split documents into chunks using `RecursiveCharacterTextSplitter`
* Generated embeddings using Gemini Embeddings
* Stored embeddings in a FAISS vector store
* Retrieved relevant chunks based on user queries
* Used Gemini to answer questions from retrieved context
* Displayed the source chunks used to generate answers

## Workflow

```text
PDF
↓
Document Loader
↓
Chunks
↓
Embeddings
↓
FAISS Vector Store
↓
Retriever
↓
Relevant Chunks
↓
Gemini
↓
Answer
```

## Technologies Used

* Python
* LangChain
* Google Gemini API
* FAISS
* PyPDFLoader
* python-dotenv

## Installation

```bash
pip install langchain
pip install langchain-community
pip install langchain-google-genai
pip install faiss-cpu
pip install pypdf
pip install python-dotenv
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Run

```bash
python RAG_demo.py
```

## What I Learned

* Document loading and processing
* Text chunking and chunk overlap
* Embeddings and vector representations
* Vector databases (FAISS)
* Similarity search and retrieval
* Retrieval-Augmented Generation (RAG)
* Prompting LLMs using retrieved context

## Limitations

* Works with a single PDF at a time
* Retrieval quality depends on chunk size and embeddings
* Can only answer questions based on the uploaded document
* Does not maintain conversation memory
