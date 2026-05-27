# Advanced Calculator 🧮

A feature-rich, professional-grade calculator with a beautiful modern GUI, scientific functions, and advanced mathematical operations. Built with Python and Tkinter.

![Status](https://img.shields.io/badge/status-production-brightgreen)
![Python](https://img.shields.io/badge/python-3.6+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Features

### Standard Calculator
- ✅ **Basic Operations** - Addition, Subtraction, Multiplication, Division
- ✅ **Decimal Support** - Full floating-point calculations
- ✅ **Parentheses** - Complex expression evaluation
- ✅ **Percentage** - Quick percentage calculations
- ✅ **Backspace** - Delete individual characters (⌫)
- ✅ **Clear Functions** - CE (Clear Entry) and C (Clear All)

### Scientific Functions
- ✅ **Trigonometric** - sin, cos, tan, asin, acos, atan
- ✅ **Logarithmic** - log (base 10), ln (natural log)
- ✅ **Power Operations** - x², x³, x^y, √x
- ✅ **Factorial** - n! (for non-negative integers)
- ✅ **Mathematical Constants** - π (pi), e (Euler's number)
- ✅ **Angle Modes** - Switch between Degree and Radian modes

### Advanced Features
- ✅ **Memory Functions** - M+, M-, MR (Memory Recall), MC (Memory Clear), MS (Memory Set)
- ✅ **Calculation History** - View last 10 calculations in real-time
- ✅ **Keyboard Support** - Full keyboard navigation (numbers, operators, Enter, Backspace, Escape)
- ✅ **Live Preview** - See results as you type
- ✅ **Error Handling** - Comprehensive error messages for invalid operations
- ✅ **Beautiful Dark Theme** - Modern dark UI with color-coded buttons

### User Interface
- 🎨 **Modern Dark Theme** - Easy on the eyes with color-coded buttons
- 🎮 **Intuitive Layout** - Organized button arrangement
- 📝 **Live History Panel** - Track your calculations
- 🖱️ **Both GUI and Keyboard Input** - Click buttons or use keyboard
- 🔄 **Mode Toggle** - Switch between Standard and Scientific modes

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (included with Python on most systems)
- No external dependencies required!

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShahabAhmed01/simple-calculator.git
   cd simple-calculator
   ```

2. **Run the Advanced Calculator:**
   ```bash
   python calculator_advanced.py
   ```

   Or run the original simple calculator:
   ```bash
   python calculator.py
   ```

## 📖 Usage Guide

### Basic Operations

1. **Launch the application:**
   ```bash
   python calculator_advanced.py
   ```

2. **Standard Mode:**
   - Click number buttons to enter numbers
   - Click operators (+, -, *, /) to perform operations
   - Click = to calculate
   - Click C to clear everything, CE to clear entry

3. **Scientific Mode:**
   - Click "Scientific" button to toggle scientific functions
   - Use trigonometric functions: sin, cos, tan, asin, acos, atan
   - Use logarithmic functions: log (base 10), ln (natural log)
   - Use power functions: x², x³, x^y, √x
   - Use factorial: ! (for non-negative integers)
   - Insert constants: π, e

4. **Memory Operations:**
   - **M+**: Add current value to memory
   - **M-**: Subtract current value from memory
   - **MR**: Recall value from memory
   - **MC**: Clear memory
   - **MS**: Set memory to current value

5. **Angle Mode:**
   - Use the dropdown to switch between DEG (Degrees) and RAD (Radians)
   - Affects trigonometric calculations

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Enter numbers |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `.` | Decimal point |
| `Enter` | Calculate result |
| `Backspace` | Delete last digit |
| `Escape` | Clear all (same as C) |

## 📁 Project Structure

```
simple-calculator/
├── calculator_advanced.py    # Advanced GUI calculator (Tkinter)
├── calculator_engine.py      # Calculation engine with math functions
├── calculator.py             # Original simple CLI calculator
├── README.md                 # This documentation
└── .gitignore                # Git ignore rules
```

## 🔧 Technical Details

### Calculator Engine (`calculator_engine.py`)
- Handles all mathematical calculations
- Scientific function implementations
- Memory management
- Angle mode conversions
- Error handling for invalid operations
- Safe expression evaluation

### Advanced GUI (`calculator_advanced.py`)
- Built with Tkinter (Python's standard GUI library)
- Modern dark theme design
- Real-time calculation display
- History tracking
- Keyboard event binding
- Responsive button layout

## 💡 Usage Examples

### Basic Arithmetic
```
Input: 25 + 15
Output: 40

Input: 100 * 0.5
Output: 50

Input: (20 + 5) * 2
Output: 50
```

### Scientific Operations
```
Input: sin(90)    [Degree mode]
Output: 1.0

Input: √16
Output: 4.0

Input: 2 ^ 10
Output: 1024

Input: 5!
Output: 120
```

### Memory Operations
```
1. Enter 50 → M+ (Memory = 50)
2. Enter 30 → M+ (Memory = 80)
3. MR (Displays 80)
4. MC (Memory = 0)
```

## 🎓 Learning Concepts

This project demonstrates:
- **Object-Oriented Programming** - Class design and method organization
- **GUI Development** - Tkinter widget creation and event handling
- **Mathematical Functions** - Trigonometry, logarithms, powers
- **Error Handling** - Try/except blocks and validation
- **String Formatting** - Format and display numerical results
- **Keyboard Events** - Binding and processing keyboard input
- **Data Structures** - History list management
- **User Experience** - Theme design and intuitive UI

## 🐛 Error Handling

The calculator gracefully handles:
- Division by zero
- Invalid mathematical domains (e.g., sqrt of negative, log of negative)
- Unbalanced parentheses
- Invalid characters in expressions
- Type errors in scientific functions

## 🔮 Future Enhancements

- Unit conversion (km to miles, Celsius to Fahrenheit, etc.)
- Graphing capabilities for functions
- Save calculation history to file
- Themes customization (Light, Dark, Custom)
- RPN (Reverse Polish Notation) mode
- Statistics functions (mean, median, std dev)
- Complex number support
- Programmable buttons with custom functions

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the **MIT License**.

## 👨‍💻 Author

Created by **Shahab Ahmed** as an advanced Python learning project.

---

## 📞 Support

If you encounter any issues:
1. Check that Python 3.6+ is installed
2. Ensure Tkinter is available (`python -m tkinter` should open a window)
3. Try running from the command line to see error messages
4. Verify all files are in the same directory

---

**Enjoy your powerful, feature-rich calculator! 🎉**

*Give this project a ⭐ if you found it helpful!*
