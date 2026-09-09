"""05 - Create a reusable prompt-model-parser chain."""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a concise learning assistant."),
        (
            "human",
            "Create a study plan for learning {subject} in {days} days.",
        ),
    ]
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0.2,
)
parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({"subject": "LangChain", "days": 7})
print(result)
