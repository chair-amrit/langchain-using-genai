from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader
import os

load_dotenv()

path=input("Enter the path of the PDF file to summarize: ").strip().strip('"')

try:
    reader=PdfReader(path)

    text=""

    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text+"\n"

    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
    )

    prompt=ChatPromptTemplate.from_template(
        """
        Summarize the following PDF in 10 concise bullet points:
        {data}
        """
    )

    chain = prompt | llm

    response=chain.invoke(
        {"data":text}
    )

    print(response.content)

except FileNotFoundError:
    print("PDF file not found.")

except Exception as e:
    print("Error:",e)