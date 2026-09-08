from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from app.tools import calculator


def create_calculator_agent():

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    tools = [
        calculator
    ]

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt="""
        You are a helpful AI calculator assistant.

        Your responsibilities:

        1. Answer normal conversational questions.
        2. Use the calculator tool whenever the user asks
           for a mathematical calculation.
        3. Never calculate complex arithmetic manually when
           the calculator tool can be used.
        4. Remember information from the conversation history.
        5. Give clear and concise answers.
        """
    )

    return agent