from arithmetic_operations import add, subtract, multiply, divide, power
from input_validation import is_numeric

def get_user_input():
    """Prompts the user for an operation and two numeric values."""
    operation = input("Choose an operation (add, subtract, multiply, divide, power): ")
    value1 = input("Enter the first number: ")
    value2 = input("Enter the second number: ")
    return operation, value1, value2

def perform_operation(operation, a, b):
    """Calls the appropriate arithmetic function based on the operation."""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power
    }
    if operation in operations:
        return operations[operation](a, b)
    else:
        raise ValueError("Invalid operation.")