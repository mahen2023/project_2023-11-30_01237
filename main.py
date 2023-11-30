from user_interface import get_user_input, perform_operation
from input_validation import is_numeric

def main():
    """Initializes the calculator application and contains the application loop."""
    while True:
        operation, value1, value2 = get_user_input()
        if not is_numeric(value1) or not is_numeric(value2):
            print("Both inputs must be numeric.")
            continue
        result = perform_operation(operation, float(value1), float(value2))
        print(f"The result is: {result}")
        if input("Do you want to perform another operation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()