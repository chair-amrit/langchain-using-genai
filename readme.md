# LangChain PDF Processing

A beginner-friendly project demonstrating document processing using LangChain and Gemini.

## Features

* Load PDF files using `PyPDFLoader`
* Extract document content and metadata
* Split documents into chunks using `RecursiveCharacterTextSplitter`
* Generate PDF summaries using Gemini
* Translate summaries to Hindi
* Display chunk count and sample chunks

## Tech Stack

* Python
* LangChain
* Gemini 2.5 Flash
* PyPDFLoader
* PyPDF2
* python-dotenv

## Workflow

```text
PDF
↓
Document Loader
↓
Document Objects
↓
Text Splitter
↓
Chunks
↓
Prompt Template
↓
Gemini
↓
Summary
↓
Hindi Translation
```

## Installation

```bash
pip install langchain
pip install langchain-community
pip install langchain-google-genai
pip install pypdf
pip install PyPDF2
pip install python-dotenv
```

## Environment Variable

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Run

```bash
python main.py
```

## Concepts Learned

* Document Loaders
* Document Objects
* Metadata
* Text Chunking
* Chunk Overlap
* Prompt Templates
* LangChain Chains
* Multi-Step Chains
* Gemini Integration
* Basic Document Processing Pipeline

```
```
