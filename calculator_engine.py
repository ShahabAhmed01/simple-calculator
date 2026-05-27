"""
Advanced Calculator Engine
Provides mathematical operations for the calculator application.
Includes scientific, trigonometric, and advanced mathematical functions.
"""

import math
import re
from typing import Union, Tuple


class CalculatorEngine:
    """Handles all mathematical calculations and operations."""

    def __init__(self):
        self.memory = 0
        self.angle_mode = "degree"  # 'degree' or 'radian'
        self.last_result = 0

    def set_angle_mode(self, mode: str):
        """Set angle mode to degree or radian."""
        self.angle_mode = mode.lower()

    def convert_angle(self, value: float) -> float:
        """Convert angle to radians if in degree mode."""
        if self.angle_mode == "degree":
            return math.radians(value)
        return value

    def convert_angle_back(self, value: float) -> float:
        """Convert angle from radians to degrees if in degree mode."""
        if self.angle_mode == "degree":
            return math.degrees(value)
        return value

    def sin(self, value: float) -> float:
        """Calculate sine."""
        try:
            return math.sin(self.convert_angle(value))
        except Exception as e:
            raise ValueError(f"Sin error: {str(e)}")

    def cos(self, value: float) -> float:
        """Calculate cosine."""
        try:
            return math.cos(self.convert_angle(value))
        except Exception as e:
            raise ValueError(f"Cos error: {str(e)}")

    def tan(self, value: float) -> float:
        """Calculate tangent."""
        try:
            return math.tan(self.convert_angle(value))
        except Exception as e:
            raise ValueError(f"Tan error: {str(e)}")

    def asin(self, value: float) -> float:
        """Calculate inverse sine."""
        try:
            if -1 <= value <= 1:
                return self.convert_angle_back(math.asin(value))
            else:
                raise ValueError("asin domain: -1 to 1")
        except Exception as e:
            raise ValueError(f"Asin error: {str(e)}")

    def acos(self, value: float) -> float:
        """Calculate inverse cosine."""
        try:
            if -1 <= value <= 1:
                return self.convert_angle_back(math.acos(value))
            else:
                raise ValueError("acos domain: -1 to 1")
        except Exception as e:
            raise ValueError(f"Acos error: {str(e)}")

    def atan(self, value: float) -> float:
        """Calculate inverse tangent."""
        try:
            return self.convert_angle_back(math.atan(value))
        except Exception as e:
            raise ValueError(f"Atan error: {str(e)}")

    def log(self, value: float) -> float:
        """Calculate base-10 logarithm."""
        try:
            if value <= 0:
                raise ValueError("log domain: x > 0")
            return math.log10(value)
        except Exception as e:
            raise ValueError(f"Log error: {str(e)}")

    def ln(self, value: float) -> float:
        """Calculate natural logarithm."""
        try:
            if value <= 0:
                raise ValueError("ln domain: x > 0")
            return math.log(value)
        except Exception as e:
            raise ValueError(f"Ln error: {str(e)}")

    def sqrt(self, value: float) -> float:
        """Calculate square root."""
        try:
            if value < 0:
                raise ValueError("sqrt domain: x >= 0")
            return math.sqrt(value)
        except Exception as e:
            raise ValueError(f"Sqrt error: {str(e)}")

    def power(self, base: float, exponent: float) -> float:
        """Calculate base to the power of exponent."""
        try:
            return base ** exponent
        except Exception as e:
            raise ValueError(f"Power error: {str(e)}")

    def factorial(self, value: float) -> float:
        """Calculate factorial."""
        try:
            if value < 0:
                raise ValueError("factorial: n >= 0")
            if not isinstance(value, int) or value != int(value):
                raise ValueError("factorial: n must be integer")
            return math.factorial(int(value))
        except Exception as e:
            raise ValueError(f"Factorial error: {str(e)}")

    def percentage(self, value: float) -> float:
        """Convert to percentage."""
        return value / 100

    def evaluate(self, expression: str) -> Union[float, str]:
        """
        Evaluate mathematical expression safely.
        Returns result or error message.
        """
        try:
            if not expression or expression.isspace():
                return "0"

            expression = expression.strip()

            # Replace common mathematical constants
            expression = expression.replace("π", str(math.pi))
            expression = expression.replace("e", str(math.e))

            # Validate expression - only allow safe characters
            safe_chars = set("0123456789+-/*().% ")
            if not all(c in safe_chars for c in expression):
                raise ValueError("Invalid characters in expression")

            # Check for balanced parentheses
            if expression.count("(") != expression.count(")"):
                raise ValueError("Unbalanced parentheses")

            # Evaluate using Python's eval (safe due to character filtering)
            result = eval(expression)

            self.last_result = float(result)
            return float(result)

        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError as e:
            return f"Error: {str(e)}"
        except SyntaxError:
            return "Error: Invalid expression"
        except Exception as e:
            return f"Error: {str(e)}"

    def memory_add(self, value: float):
        """Add value to memory."""
        self.memory += value

    def memory_subtract(self, value: float):
        """Subtract value from memory."""
        self.memory -= value

    def memory_recall(self) -> float:
        """Recall memory value."""
        return self.memory

    def memory_clear(self):
        """Clear memory."""
        self.memory = 0

    def memory_set(self, value: float):
        """Set memory to specific value."""
        self.memory = value
