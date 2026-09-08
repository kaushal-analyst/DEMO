from dotenv import load_dotenv

from app.agent import create_calculator_agent
from app.memory import ConversationMemory


# Load environment variables from .env
load_dotenv()


def main():

    print("=" * 60)
    print("       AI CALCULATOR ASSISTANT")
    print("=" * 60)

    print("\nType 'exit' to quit.")
    print("Type 'clear' to clear conversation memory.\n")

    agent = create_calculator_agent()

    memory = ConversationMemory()

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        # Exit
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Clear memory
        if user_input.lower() == "clear":
            memory.clear()
            print("\nConversation memory cleared.\n")
            continue

        # Add user message to memory
        memory.add_user_message(user_input)

        try:

            result = agent.invoke(
                {
                    "messages": memory.get_messages()
                }
            )

            # Get final AI message
            ai_message = result["messages"][-1]

            response = ai_message.content

            print(f"AI: {response}\n")

            # Add AI response to memory
            memory.add_ai_message(response)

        except Exception as e:

            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()