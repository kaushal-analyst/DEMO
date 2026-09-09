"""06 - Print model output as it arrives."""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in a clear, beginner-friendly way."
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)
chain = prompt | model

for chunk in chain.stream({"topic": "LangChain streaming"}):
    print(chunk.content, end="", flush=True)
print()
