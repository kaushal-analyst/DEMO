"""04 - Build a prompt from runtime values."""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a {role}. Use a {tone} tone and keep the answer concise.",
        ),
        ("human", "Help me understand: {question}"),
    ]
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)

chain = prompt | model
response = chain.invoke(
    {
        "role": "Python tutor",
        "tone": "friendly",
        "question": "What is a Python list comprehension?",
    }
)
print(response.content)
