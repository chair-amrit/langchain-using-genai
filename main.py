from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader

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

    prompt1=ChatPromptTemplate.from_template(
        """
        Summarize the following PDF in 3 concise bullet points:
        {data}
        """
    )

    prompt2=ChatPromptTemplate.from_template(
        """
        Translate the following text into hindi:
        {data}
        """
    )

    chain1 = prompt1 | llm

    chain2 = prompt2 | llm

    response1=chain1.invoke(
        {"data":text}
    )

    response2=chain2.invoke(
        {"data":response1.content}
    )

    print("========== Summary ==========")
    print(response1.content)
    print("========== Translation in Hindi ==========")
    print(response2.content)

except FileNotFoundError:
    print("PDF file not found.")

except Exception as e:
    print("Error:",e)