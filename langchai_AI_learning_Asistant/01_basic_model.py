"""01 - Call a chat model directly."""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)

response = model.invoke("Explain what LangChain is in one short paragraph.")
print(response.content)
