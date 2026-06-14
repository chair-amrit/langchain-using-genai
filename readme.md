# LangChain PDF Summarizer

A simple AI-powered PDF summarizer built using PyPDF2, LangChain, and Gemini.

## Features

* Reads a PDF file from a user-provided path
* Extracts text from all pages
* Uses a LangChain PromptTemplate
* Sends the extracted text to Gemini 2.5 Flash
* Generates a concise summary in 10 bullet points

## Technologies

* Python
* PyPDF2
* LangChain
* Gemini API
* python-dotenv

## Workflow

```text
PDF
↓
Text Extraction
↓
PromptTemplate
↓
LangChain Chain
↓
Gemini LLM
↓
Summary
```

## Installation

```bash
pip install pypdf2
pip install langchain
pip install langchain-google-genai
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

## Learning Outcomes

* PDF text extraction
* Prompt engineering
* LangChain chains
* LLM integration
* End-to-end document processing

```
```
