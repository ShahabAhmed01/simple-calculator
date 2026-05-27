# Advance Calculator 🧮

<div align="center">

**A professional-grade calculator with beautiful GUI, scientific functions, and advanced features**

[![Status](https://img.shields.io/badge/status-production-brightgreen?style=flat-square)](https://github.com/ShahabAhmed01/advance-calculator)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Code Quality](https://img.shields.io/badge/code%20quality-production%2Dready-brightgreen?style=flat-square)]()
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-blue?style=flat-square)]()

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 📸 Quick Look

A powerful calculator with an intuitive dark-themed interface featuring:
- 🎯 **25+ mathematical operations** (basic, scientific, trigonometric)
- 💾 **Advanced memory functions** for efficient calculations
- ⌨️ **Full keyboard support** for faster input
- 📊 **Real-time calculation history** tracking
- 🎨 **Beautiful dark UI** with color-coded buttons
- 🛡️ **Robust error handling** for safe operations

---

## ✨ Features

### 🔢 Standard Operations
- ✅ Basic arithmetic: addition (+), subtraction (-), multiplication (*), division (/)
- ✅ Decimal number support with floating-point precision
- ✅ Parentheses for complex expression grouping
- ✅ Percentage calculations
- ✅ Backspace (⌫) for digit-by-digit editing
- ✅ Multiple clear modes: CE (Clear Entry), C (Clear All)

### 🧪 Scientific Functions
- ✅ **Trigonometric**: sin, cos, tan, asin, acos, atan
- ✅ **Logarithmic**: log (base 10), ln (natural logarithm)
- ✅ **Power operations**: x², x³, x^y, √x (square root)
- ✅ **Factorial**: n! (for non-negative integers)
- ✅ **Mathematical constants**: π (pi), e (Euler's number)
- ✅ **Angle modes**: Toggle between Degrees and Radians

### 🚀 Advanced Features
- ✅ **Memory management**: M+, M-, MR (Memory Recall), MC (Memory Clear), MS (Memory Set)
- ✅ **Calculation history**: View and track last 10 calculations in real-time
- ✅ **Live preview**: See results instantly as you type
- ✅ **Keyboard support**: Full keyboard navigation for numbers, operators, and functions
- ✅ **Two modes**: Toggle between Standard and Scientific calculator modes
- ✅ **Smart error handling**: Comprehensive, user-friendly error messages

### 🎨 User Interface
- ✅ Modern dark theme - easy on the eyes
- ✅ Color-coded buttons for quick recognition
  - 🟠 Orange: operators
  - 🟣 Purple: scientific functions
  - 🟤 Brown: memory functions
  - 🔴 Red: clear/delete
- ✅ Large, readable dual-line display
- ✅ Responsive, intuitive button layout
- ✅ Both mouse and keyboard input support

---

## 🚀 Installation

### Prerequisites
- **Python** 3.6 or higher
- **Tkinter** (included with Python on most systems)
- **No external dependencies required!**

### Quick Start

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShahabAhmed01/advance-calculator.git
cd advance-calculator
```

#### 2️⃣ Run the Calculator
```bash
python calculator_advanced.py
```

That's it! The advanced calculator GUI will launch.

### Alternative: Simple CLI Calculator
```bash
python calculator.py
```

### Troubleshooting Installation

**Missing Tkinter?**
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **Fedora**: `sudo dnf install python3-tkinter`
- **Arch Linux**: `sudo pacman -S tk`
- **macOS**: Tkinter is included with Python from python.org
- **Windows**: Reinstall Python and ensure Tkinter is selected

---

## 📖 Usage Guide

### Launching the Calculator
```bash
python calculator_advanced.py
```

### Standard Mode (Default)
1. **Enter numbers** by clicking buttons or using keyboard (0-9)
2. **Choose an operation** (+, -, *, /)
3. **Press Enter** or click = to calculate
4. **Use CE** to clear current entry or **C** to clear everything

### Scientific Mode
1. Click **Scientific** button to expand scientific functions
2. Access advanced operations:
   - **Trigonometric**: sin, cos, tan, asin, acos, atan
   - **Logarithmic**: log (base 10), ln (natural)
   - **Power**: x², x³, x^y, √x
   - **Factorial**: n!
   - **Constants**: π, e

### Memory Operations
- **M+**: Add current value to memory
- **M-**: Subtract current value from memory
- **MR**: Recall stored memory value
- **MC**: Clear memory to 0
- **MS**: Set memory to current value

### Angle Mode Selection
Use the **Angle** dropdown to switch between:
- **DEG**: Degrees (default)
- **RAD**: Radians (for advanced calculations)

### Keyboard Shortcuts

| Keyboard | Action | Keyboard | Action |
|----------|--------|----------|--------|
| `0` - `9` | Enter digits | `+` | Addition |
| `-` | Subtraction | `*` | Multiplication |
| `/` | Division | `.` | Decimal point |
| `Enter` | Calculate | `Backspace` | Delete digit |
| `Escape` | Clear all | | |

---

## 💡 Usage Examples

### Basic Arithmetic
```
25 + 15 = 40
100 * 0.5 = 50
(20 + 5) * 2 = 50
144 / 12 = 12
```

### Scientific Operations
```
sin(90°) = 1.0
cos(0°) = 1.0
√16 = 4.0
2^10 = 1024
5! = 120
log(100) = 2.0
ln(e) = 1.0
```

### Memory Functions Workflow
```
1. Calculate: 50 + 30 = 80
2. Store: M+ (Memory = 80)
3. New calculation: 20 * 5 = 100
4. Add to memory: M+ (Memory = 180)
5. Recall: MR → Displays 180
```

---

## 📁 Project Structure

```
advance-calculator/
├── calculator_advanced.py      # GUI application (Tkinter) - Main entry point
├── calculator_engine.py        # Mathematical engine with all operations
├── calculator.py               # Simple CLI calculator (original)
├── test_calculator.py          # Comprehensive test suite
├── setup.py                    # Setup and deployment script
├── README.md                   # This documentation
├── FEATURES.md                 # Complete feature checklist
├── MAKE_PUBLIC.md              # Public repository instructions
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore configuration
```

---

## 🔧 Technical Details

### Architecture

**calculator_engine.py** - Mathematical Engine
- ✓ Safe expression evaluation with input validation
- ✓ 25+ mathematical functions
- ✓ Memory state management
- ✓ Angle mode conversion (degree/radian)
- ✓ Comprehensive error handling
- ✓ Domain validation for trigonometric and logarithmic functions

**calculator_advanced.py** - GUI Application
- ✓ Built with Tkinter (Python standard library)
- ✓ Modern dark theme design
- ✓ Real-time display updates
- ✓ Event-driven keyboard input
- ✓ Responsive UI layout
- ✓ History tracking system

### Dependencies
**Zero external dependencies!** Only uses Python built-in modules:
- `tkinter` - GUI framework
- `math` - Mathematical functions
- `typing` - Type hints
- Standard library modules

---

## 🧪 Testing

### Run Test Suite
```bash
python test_calculator.py
```

Or use the setup script:
```bash
python setup.py test
```

### What's Tested
✅ Basic arithmetic operations
✅ Decimal number handling
✅ Scientific functions
✅ Trigonometric calculations
✅ Logarithmic operations
✅ Memory functions
✅ Error handling (division by zero, domain errors)
✅ Complex expressions with parentheses

---

## 🎓 Learning Value

This project demonstrates professional Python development practices:

- **Object-Oriented Programming**: Clean class design and method organization
- **GUI Development**: Tkinter widgets, event handling, responsive design
- **Mathematical Programming**: Implementation of complex functions
- **Error Handling**: Comprehensive validation and exception handling
- **Code Organization**: Separation of concerns (UI + Engine)
- **Testing**: Test-driven development with comprehensive test coverage
- **Documentation**: Professional documentation practices

---

## 🐛 Error Handling

The calculator gracefully handles:
- ✓ Division by zero
- ✓ Invalid mathematical domains (negative square root, log of negative)
- ✓ Unbalanced parentheses
- ✓ Invalid character input
- ✓ Type conversion errors
- ✓ Out-of-range calculations
- ✓ All errors display user-friendly messages

---

## 🔮 Future Enhancements

- 📐 Unit conversion (length, weight, temperature, etc.)
- 📊 Graphing capabilities for functions and data
- 💾 Save/load calculation history to file
- 🎨 Multiple themes (Light, Dark, Custom)
- 🔄 RPN (Reverse Polish Notation) mode
- 📈 Statistics functions (mean, median, standard deviation)
- 🔢 Complex number support
- ⌨️ Customizable keyboard layouts
- 📱 Mobile-friendly version

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 10 |
| **Lines of Code** | ~800 |
| **Functions** | 25+ |
| **Test Cases** | 25+ |
| **External Dependencies** | 0 |
| **Python Version** | 3.6+ |
| **Git Commits** | 10+ |
| **Code Quality** | Production-Ready ✅ |

---

## 🤝 Contributing

We welcome contributions! Feel free to:

1. **Report bugs** - [Create an issue](https://github.com/ShahabAhmed01/advance-calculator/issues)
2. **Suggest features** - Share your ideas for improvements
3. **Submit pull requests** - Send your enhancements
4. **Improve documentation** - Help make it clearer
5. **Share feedback** - Let us know what you think

### Development Guidelines
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation accordingly
- Use clear, descriptive commit messages

---

## 📄 License

This project is open source and available under the **MIT License**.

```
MIT License

Copyright (c) 2024 Shahab Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

See [LICENSE](LICENSE) for full details.

---

## 👨‍💻 Author

**Shahab Ahmed**
- GitHub: [@ShahabAhmed01](https://github.com/ShahabAhmed01)
- Project: Advance Calculator - Professional-grade mathematical tool

---

## 📞 Support & Help

### Getting Help
1. **Check documentation**: See [README.md](README.md) and [FEATURES.md](FEATURES.md)
2. **Review examples**: Check [Usage Examples](#-usage-examples) section
3. **Run tests**: `python test_calculator.py` to verify installation
4. **Create issue**: Report problems on GitHub Issues

### Common Issues

**Calculator won't start?**
- Verify Python 3.6+ is installed: `python --version`
- Check Tkinter availability: `python -m tkinter`
- Ensure all files are in the same directory

**Tkinter not found?**
- Install Tkinter for your OS (see [Installation](#-installation))

**Tests failing?**
- Run from project directory: `python test_calculator.py`
- Check error messages for specific failures

---

<div align="center">

### 🌟 If you find this project useful, please give it a star! ⭐

[Star on GitHub](https://github.com/ShahabAhmed01/advance-calculator) • [Report Bug](https://github.com/ShahabAhmed01/advance-calculator/issues) • [Request Feature](https://github.com/ShahabAhmed01/advance-calculator/issues)

**Made with ❤️ by Shahab Ahmed**

</div>
