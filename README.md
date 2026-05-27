# Simple Calculator 🧮

A beginner-friendly Python calculator script that performs basic arithmetic operations. Perfect for learning Python fundamentals!

## Features

- ✅ **Addition** - Add two numbers
- ✅ **Subtraction** - Subtract two numbers
- ✅ **Multiplication** - Multiply two numbers
- ✅ **Division** - Divide two numbers (with zero-division protection)
- ✅ **Interactive Menu** - User-friendly command-line interface
- ✅ **Error Handling** - Validates input and handles edge cases

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required!

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShahabAhmed01/simple-calculator.git
   cd simple-calculator
   ```

2. **Run the calculator:**
   ```bash
   python calculator.py
   ```

## Usage

Simply run the script and follow the on-screen prompts:

```
========================================
Welcome to Simple Calculator!
========================================

Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
----------------------------------------

Enter choice (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5

10.0 + 5.0 = 15.0
```

## Project Structure

```
simple-calculator/
├── calculator.py      # Main calculator script
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Learning Concepts

This project demonstrates:
- Functions and function parameters
- While loops
- Conditional statements (if/elif/else)
- User input handling
- Error handling (try/except)
- String formatting
- Docstrings and comments

## Code Example

Here's a simple example of using the calculator functions directly in Python:

```python
from calculator import add, subtract, multiply, divide

# Use the functions directly
result = add(10, 5)
print(result)  # Output: 15

result = multiply(4, 3)
print(result)  # Output: 12
```

## Future Enhancements

- Add more advanced operations (power, square root, modulo)
- Save calculation history
- Implement a GUI using tkinter
- Add unit tests
- Support for complex numbers

## License

This project is open source and available under the MIT License.

## Author

Created by Shahab Ahmed as a beginner Python learning project.

---

**Happy Calculating! 🎉**
