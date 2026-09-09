"""02 - Combine a prompt template with a chat model."""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You explain technical topics clearly for beginners."),
        ("human", "Explain {topic} using a simple example."),
    ]
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)

messages = prompt.invoke({"topic": "LangChain prompts"})
response = model.invoke(messages)
print(response.content)
