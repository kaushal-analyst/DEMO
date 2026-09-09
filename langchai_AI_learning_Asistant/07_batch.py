"""07 - Run the same chain for multiple inputs."""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Define {term} in one sentence for a beginner."
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)
chain = prompt | model | StrOutputParser()

terms = [{"term": term} for term in ["chain", "prompt", "output parser"]]
results = chain.batch(terms)

for term, result in zip(terms, results):
    print(f"{term['term']}: {result}")
