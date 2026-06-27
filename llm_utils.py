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
        Conversation History:
        {messages}

        Document Context:
        {context}

        Current Question:
        {question}

        Use the conversation history only to resolve references such as "it", "they", "those", etc.
        Answer using the document context or anything given in history. If the answer is not present, return NOT_FOUND.

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




from langchain_groq import ChatGroq

def router_chain(query):
    llm=ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )
    prompt=ChatPromptTemplate.from_template(
        """
        Classify the user input into exactly one category:

        chat: greetings, casual conversation, questions about the assistant, small talk.
        doc: information-seeking questions, technical questions, or questions that may require document or web knowledge.
        nonsense: gibberish or meaningless input.

        Return ONLY one word:
        chat
        doc
        nonsense

        Input:
        {query}
"""
    )
    return prompt | llm