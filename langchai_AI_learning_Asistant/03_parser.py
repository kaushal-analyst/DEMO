"""03 - Parse a model message into plain text."""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Give three practical tips for learning {topic}."
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "Python"})
print(result)
