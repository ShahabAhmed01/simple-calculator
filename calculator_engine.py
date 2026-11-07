"""Mathematical engine for Simple Calculator.

The evaluator accepts arithmetic expressions containing numbers, parentheses,
and the operators ``+ - * / % ^``. It parses the expression with :mod:`ast` and
walks a small whitelist of numeric nodes instead of using :func:`eval`, so a
malformed expression cannot execute arbitrary Python code.
"""

from __future__ import annotations

import ast
import math
import operator
import re

Number = int | float

_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


class CalculatorEngine:
    """Handles all mathematical calculations and operations."""

    MAX_EXPRESSION_LENGTH = 200
    MAX_FACTORIAL = 170
    MAX_EXPONENT = 1000
    MAX_RESULT = 1e308

    def __init__(self) -> None:
        self.memory = 0.0
        self.angle_mode = "degree"  # 'degree' or 'radian'
        self.last_result = 0.0

    def set_angle_mode(self, mode: str) -> None:
        """Set angle mode to degree or radian."""
        aliases = {
            "deg": "degree",
            "degree": "degree",
            "rad": "radian",
            "radian": "radian",
        }
        normalized = mode.lower()
        if normalized not in aliases:
            raise ValueError("Angle mode must be 'degree' or 'radian'")
        self.angle_mode = aliases[normalized]

    def convert_angle(self, value: float) -> float:
        """Convert an angle to radians when the engine is in degree mode."""
        if self.angle_mode == "degree":
            return math.radians(value)
        return value

    def convert_angle_back(self, value: float) -> float:
        """Convert a result in radians back to degrees in degree mode."""
        if self.angle_mode == "degree":
            return math.degrees(value)
        return value

    def sin(self, value: float) -> float:
        """Calculate sine."""
        return math.sin(self.convert_angle(value))

    def cos(self, value: float) -> float:
        """Calculate cosine."""
        return math.cos(self.convert_angle(value))

    def tan(self, value: float) -> float:
        """Calculate tangent, rejecting angles where it is undefined."""
        angle = self.convert_angle(value)
        if abs(math.cos(angle)) < 1e-12:
            raise ValueError("tan is undefined at this angle")
        return math.tan(angle)

    def asin(self, value: float) -> float:
        """Calculate inverse sine."""
        if not -1 <= value <= 1:
            raise ValueError("asin is defined only for values between -1 and 1")
        return self.convert_angle_back(math.asin(value))

    def acos(self, value: float) -> float:
        """Calculate inverse cosine."""
        if not -1 <= value <= 1:
            raise ValueError("acos is defined only for values between -1 and 1")
        return self.convert_angle_back(math.acos(value))

    def atan(self, value: float) -> float:
        """Calculate inverse tangent."""
        return self.convert_angle_back(math.atan(value))

    def log(self, value: float) -> float:
        """Calculate base-10 logarithm."""
        if value <= 0:
            raise ValueError("log is defined only for values greater than 0")
        return math.log10(value)

    def ln(self, value: float) -> float:
        """Calculate natural logarithm."""
        if value <= 0:
            raise ValueError("ln is defined only for values greater than 0")
        return math.log(value)

    def sqrt(self, value: float) -> float:
        """Calculate square root."""
        if value < 0:
            raise ValueError("sqrt is defined only for values greater than or equal to 0")
        return math.sqrt(value)

    def power(self, base: float, exponent: float) -> float:
        """Calculate base to the power of exponent."""
        if not math.isfinite(base) or not math.isfinite(exponent):
            raise ValueError("Power requires finite numbers")
        if abs(exponent) > self.MAX_EXPONENT:
            raise ValueError("Exponent is too large")
        result = base**exponent
        if isinstance(result, complex):
            raise ValueError("Complex results are not supported")
        if abs(result) > self.MAX_RESULT:
            raise ValueError("Result is too large")
        return result

    def factorial(self, value: float) -> int:
        """Calculate factorial for a non-negative integer value."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("factorial requires a number")
        if not math.isfinite(value) or value < 0 or value != int(value):
            raise ValueError("factorial is defined only for non-negative integers")
        if value > self.MAX_FACTORIAL:
            raise ValueError(f"factorial is limited to {self.MAX_FACTORIAL}")
        return math.factorial(int(value))

    def percentage(self, value: float) -> float:
        """Convert a value to a percentage (divide by 100)."""
        return value / 100

    def evaluate(self, expression: str) -> float | str:
        """Evaluate a mathematical expression safely.

        Returns a float on success or a user-readable ``"Error: ..."`` string.
        """
        if not isinstance(expression, str):
            return "Error: Expression must be text"
        if not expression or expression.isspace():
            return "0"

        expression = expression.strip()
        if len(expression) > self.MAX_EXPRESSION_LENGTH:
            return f"Error: Expression is limited to {self.MAX_EXPRESSION_LENGTH} characters"

        try:
            tree = ast.parse(self._normalize(expression), mode="eval")
            result = self._evaluate_node(tree.body)
            if isinstance(result, complex):
                raise ValueError("Complex results are not supported")
            if abs(result) > self.MAX_RESULT:
                raise ValueError("Result is too large")
            self.last_result = float(result)
            return float(result)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except SyntaxError:
            return "Error: Invalid expression"
        except ValueError as exc:
            return f"Error: {exc}"
        except OverflowError:
            return "Error: Result is too large"
        except Exception as exc:  # pragma: no cover - defensive fallback
            return f"Error: {exc}"

    @staticmethod
    def _normalize(expression: str) -> str:
        """Translate calculator notation into Python arithmetic notation."""
        text = expression.replace("π", str(math.pi))
        text = text.replace("×", "*").replace("÷", "/").replace("−", "-")
        text = text.replace("^", "**")
        # Replace a standalone "e" constant, but leave scientific notation
        # such as 1e3 untouched.
        return re.sub(r"(?<![0-9.])e(?![0-9.])", str(math.e), text)

    @classmethod
    def _evaluate_node(cls, node: ast.AST) -> Number:
        """Recursively evaluate a whitelisted numeric AST node."""
        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Only numbers are allowed")

        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
            operand = cls._evaluate_node(node.operand)
            return _UNARY_OPERATORS[type(node.op)](operand)

        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
            left = cls._evaluate_node(node.left)
            right = cls._evaluate_node(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > cls.MAX_EXPONENT:
                raise ValueError("Exponent is too large")
            result = _BINARY_OPERATORS[type(node.op)](left, right)
            if isinstance(result, complex):
                raise ValueError("Complex results are not supported")
            if isinstance(result, (int, float)) and abs(result) > cls.MAX_RESULT:
                raise ValueError("Result is too large")
            return result

        raise ValueError("Invalid expression")

    def memory_add(self, value: float) -> None:
        """Add value to memory."""
        self.memory += value

    def memory_subtract(self, value: float) -> None:
        """Subtract value from memory."""
        self.memory -= value

    def memory_recall(self) -> float:
        """Recall memory value."""
        return self.memory

    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = 0.0

    def memory_set(self, value: float) -> None:
        """Set memory to a specific value."""
        self.memory = value
