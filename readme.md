# LangChain PDF Processor

A document processing application built using PyPDF2, LangChain, and Gemini.

## Features

* Reads a PDF file from a user-provided path
* Extracts text from all pages
* Uses LangChain PromptTemplates
* Generates a 3-point summary of the document
* Translates the summary into Hindi
* Displays both English and Hindi outputs

## Technologies Used

* Python
* PyPDF2
* LangChain
* Gemini 2.5 Flash
* python-dotenv

## Workflow

```text
PDF
↓
Text Extraction
↓
Chain 1: Summarization
↓
English Summary
↓
Chain 2: Hindi Translation
↓
Hindi Summary
```

## Installation

```bash
pip install pypdf2
pip install langchain
pip install langchain-google-genai
pip install python-dotenv
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Run

```bash
python main.py
```

Enter the path of the PDF file when prompted.

## LangChain Concepts Demonstrated

* PromptTemplate
* LLM Integration
* Chain Creation
* Multi-step Chaining
* Output of One Chain as Input to Another
* Document Processing Pipeline

## Learning Outcomes

* PDF text extraction
* Prompt engineering
* LangChain fundamentals
* Sequential AI workflows
* Gemini API integration
* Multi-stage text transformation

```
```
