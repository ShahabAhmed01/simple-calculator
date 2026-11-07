"""Tests for the calculator engine."""

import math
import unittest

from calculator_engine import CalculatorEngine


class CalculatorEngineTests(unittest.TestCase):
    def setUp(self):
        self.engine = CalculatorEngine()

    def assert_error(self, result):
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"), result)

    def test_basic_arithmetic(self):
        self.assertEqual(self.engine.evaluate("5 + 3"), 8)
        self.assertEqual(self.engine.evaluate("10 - 4"), 6)
        self.assertEqual(self.engine.evaluate("6 * 7"), 42)
        self.assertEqual(self.engine.evaluate("20 / 4"), 5)

    def test_decimals_and_parentheses(self):
        self.assertEqual(self.engine.evaluate("10.5 + 2.5"), 13)
        self.assertEqual(self.engine.evaluate("5.5 * 2"), 11)
        self.assertEqual(self.engine.evaluate("(10 + 5) * 2"), 30)
        self.assertEqual(self.engine.evaluate("100 / (2 + 3)"), 20)

    def test_power_operator(self):
        self.assertEqual(self.engine.evaluate("2^10"), 1024)
        self.assertEqual(self.engine.evaluate("2**10"), 1024)
        self.assertEqual(self.engine.evaluate("(-2)^3"), -8)

    def test_constants_and_scientific_notation(self):
        self.assertAlmostEqual(self.engine.evaluate("π"), math.pi)
        self.assertAlmostEqual(self.engine.evaluate("e"), math.e)
        self.assertAlmostEqual(self.engine.evaluate("2*π"), 2 * math.pi)
        self.assertEqual(self.engine.evaluate("1e3"), 1000)

    def test_modulo(self):
        self.assertEqual(self.engine.evaluate("10 % 3"), 1)

    def test_empty_expression(self):
        self.assertEqual(self.engine.evaluate(""), "0")
        self.assertEqual(self.engine.evaluate("   "), "0")

    def test_division_by_zero(self):
        self.assert_error(self.engine.evaluate("1/0"))
        self.assert_error(self.engine.evaluate("10 % 0"))

    def test_invalid_expressions(self):
        self.assert_error(self.engine.evaluate("((5+3"))
        self.assert_error(self.engine.evaluate("2(3)"))
        self.assert_error(self.engine.evaluate("__import__('os')"))
        self.assert_error(self.engine.evaluate("hello"))

    def test_expression_length_limit(self):
        self.assert_error(self.engine.evaluate("1+" * 200 + "1"))

    def test_huge_exponent_is_rejected(self):
        self.assert_error(self.engine.evaluate("9^9^9"))
        self.assert_error(self.engine.evaluate("2^1024"))

    def test_factorial(self):
        self.assertEqual(self.engine.factorial(5), 120)
        self.assertEqual(self.engine.factorial(5.0), 120)
        self.assertEqual(self.engine.factorial(0), 1)
        self.assert_error(self.engine.evaluate("5!"))
        with self.assertRaises(ValueError):
            self.engine.factorial(-1)
        with self.assertRaises(ValueError):
            self.engine.factorial(2.5)
        with self.assertRaises(ValueError):
            self.engine.factorial(171)
        with self.assertRaises(ValueError):
            self.engine.factorial(True)

    def test_trigonometry_in_degrees(self):
        self.assertAlmostEqual(self.engine.sin(90), 1.0)
        self.assertAlmostEqual(self.engine.cos(0), 1.0)
        self.assertAlmostEqual(self.engine.tan(45), 1.0)
        with self.assertRaises(ValueError):
            self.engine.tan(90)

    def test_trigonometry_in_radians(self):
        self.engine.set_angle_mode("radian")
        self.assertAlmostEqual(self.engine.sin(math.pi / 2), 1.0)
        self.assertAlmostEqual(self.engine.asin(1), math.pi / 2)

    def test_inverse_trigonometry(self):
        self.assertAlmostEqual(self.engine.asin(1), 90.0)
        self.assertAlmostEqual(self.engine.acos(1), 0.0)
        self.assertAlmostEqual(self.engine.atan(1), 45.0)
        with self.assertRaises(ValueError):
            self.engine.asin(2)
        with self.assertRaises(ValueError):
            self.engine.acos(-2)

    def test_logarithms_and_square_root(self):
        self.assertEqual(self.engine.log(100), 2)
        self.assertAlmostEqual(self.engine.ln(math.e), 1.0)
        self.assertEqual(self.engine.sqrt(16), 4)
        with self.assertRaises(ValueError):
            self.engine.log(0)
        with self.assertRaises(ValueError):
            self.engine.ln(-1)
        with self.assertRaises(ValueError):
            self.engine.sqrt(-1)

    def test_power_method(self):
        self.assertEqual(self.engine.power(2, 3), 8)
        with self.assertRaises(ValueError):
            self.engine.power(-1, 0.5)
        with self.assertRaises(ValueError):
            self.engine.power(10, 1000)

    def test_percentage(self):
        self.assertEqual(self.engine.percentage(50), 0.5)

    def test_angle_mode_validation(self):
        self.engine.set_angle_mode("RAD")
        self.assertEqual(self.engine.angle_mode, "radian")
        with self.assertRaises(ValueError):
            self.engine.set_angle_mode("gradians")

    def test_memory_functions(self):
        self.engine.memory_clear()
        self.engine.memory_add(50)
        self.assertEqual(self.engine.memory_recall(), 50)
        self.engine.memory_subtract(20)
        self.assertEqual(self.engine.memory_recall(), 30)
        self.engine.memory_set(100)
        self.assertEqual(self.engine.memory_recall(), 100)
        self.engine.memory_clear()
        self.assertEqual(self.engine.memory_recall(), 0)

    def test_last_result_is_updated(self):
        self.engine.evaluate("6 * 7")
        self.assertEqual(self.engine.last_result, 42)


if __name__ == "__main__":
    unittest.main()
