from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def google_chain():
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )
    prompt= ChatPromptTemplate.from_template(
        """
        Answer the question using only provided context.
        If the answer is not present in the context, return exactly:
        NOT_FOUND
        Do not use outside knowledge.

        
        Context:
        {context}
        
        Question:
        {question}

        """
    )
    return prompt | llm


def web_chain():
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )
    prompt= ChatPromptTemplate.from_template(
        """
        Answer the question using the web search results.
        

        Web Search Results:
        {context}

        Question:
        {question}
        """
    )
    return prompt | llm



from tavily import TavilyClient
import os

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def tav_search(query):
    response = client.search(
        query=query
    )
    results=response["results"]

    context="\n\n".join(
        f"{result['title']}\n{result['content'][:400]}"
        for result in results[:5]
    )
    return context