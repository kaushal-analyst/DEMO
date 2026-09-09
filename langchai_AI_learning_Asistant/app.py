"""Small interactive learning assistant built from the lessons."""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a patient AI learning assistant. Explain concepts simply, "
            "use a short example, and suggest one practice task.",
        ),
        ("human", "Teach me about {question}"),
    ]
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0.2,
)
assistant = prompt | model | StrOutputParser()


def main() -> None:
    print("LangChain AI Learning Assistant")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("What would you like to learn? ").strip()
        if question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            return
        if not question:
            continue

        print("\nAssistant:")
        print(assistant.invoke({"question": question}))
        print()


if __name__ == "__main__":
    main()
