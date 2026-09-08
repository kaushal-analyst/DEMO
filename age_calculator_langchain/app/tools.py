from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Supports addition, subtraction, multiplication and division.
    Example: 25 * 40
    """

    try:
        allowed_characters = "0123456789+-*/(). "

        if not all(char in allowed_characters for char in expression):
            return "Error: Only basic mathematical expressions are allowed."

        result = eval(expression, {"__builtins__": {}}, {})

        return str(result)

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except Exception:
        return "Error: Invalid mathematical expression."
