"""
Simple Calculator - A beginner-friendly Python calculator script.
Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
"""


def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract two numbers."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    """Main calculator function that runs an interactive calculator."""
    print("=" * 40)
    print("Welcome to Simple Calculator!")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-" * 40)

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("\nThank you for using Simple Calculator! Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"\n{num1} + {num2} = {add(num1, num2)}\n")
                elif choice == "2":
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}\n")
                elif choice == "3":
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}\n")
                elif choice == "4":
                    print(f"\n{num1} ÷ {num2} = {divide(num1, num2)}\n")
            except ValueError:
                print("Invalid input! Please enter numeric values.\n")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    calculator()
