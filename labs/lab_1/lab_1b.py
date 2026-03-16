
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.
    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        float: The result of the operation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def get_number(prompt: str) -> float:
    """Keeps asking for input until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operation() -> str:
    """Keeps asking for input until a valid operation is entered."""
    valid_operations = {"add", "subtract", "multiply", "divide"}
    while True:
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        if operation in valid_operations:
            return operation
        print("Error: Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    print(f"===== Simple Calculator =====")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    while True:
        try:
            result = simple_calculator(operation, num1, num2)
            break
        except ValueError as e:
            print(f"Error: {e}")
            num2 = get_number("Enter the second number: ")

    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()