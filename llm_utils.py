from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

def google_chain():
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )
    prompt= ChatPromptTemplate.from_template(
        """
        Answer the question using only provided context.
        
        Context:
        {context}
        
        Question:
        {question}

        """
    )
    return prompt | llm