"""Tests for the command-line calculator."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from calculator import add, calculator, divide, multiply, subtract


class CalculatorFunctionTests(unittest.TestCase):
    def test_arithmetic_functions(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(divide(10, 5), 2)

    def test_division_by_zero_returns_message(self):
        self.assertEqual(divide(10, 0), "Error! Division by zero.")


class CalculatorLoopTests(unittest.TestCase):
    def run_with_input(self, values):
        output = io.StringIO()
        with patch("builtins.input", side_effect=values):
            with redirect_stdout(output):
                calculator()
        return output.getvalue()

    def test_exit_choice(self):
        output = self.run_with_input(["5"])
        self.assertIn("Goodbye", output)

    def test_addition_flow(self):
        output = self.run_with_input(["1", "10", "5", "5"])
        self.assertIn("10.0 + 5.0 = 15.0", output)

    def test_invalid_choice_then_exit(self):
        output = self.run_with_input(["nope", "5"])
        self.assertIn("Invalid choice", output)
        self.assertIn("Goodbye", output)

    def test_invalid_number_then_exit(self):
        output = self.run_with_input(["1", "abc", "5"])
        self.assertIn("Invalid input", output)
        self.assertIn("Goodbye", output)

    def test_eof_exits_cleanly(self):
        output = self.run_with_input([EOFError])
        self.assertIn("Goodbye", output)


if __name__ == "__main__":
    unittest.main()
