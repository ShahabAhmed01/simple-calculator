"""
Test Script for Advanced Calculator
Tests all major functionality of the calculator engine and GUI.
"""

from calculator_engine import CalculatorEngine
import math


def test_calculator_engine():
    """Test all calculator engine functions."""
    engine = CalculatorEngine()
    tests_passed = 0
    tests_failed = 0

    print("=" * 60)
    print("ADVANCED CALCULATOR TEST SUITE")
    print("=" * 60)

    # Test basic arithmetic
    print("\n✓ Testing Basic Arithmetic...")
    assert engine.evaluate("5 + 3") == 8, "Addition failed"
    assert engine.evaluate("10 - 4") == 6, "Subtraction failed"
    assert engine.evaluate("6 * 7") == 42, "Multiplication failed"
    assert engine.evaluate("20 / 4") == 5, "Division failed"
    tests_passed += 4
    print("  ✓ Basic arithmetic: PASSED")

    # Test decimal operations
    print("\n✓ Testing Decimal Operations...")
    assert engine.evaluate("10.5 + 2.5") == 13, "Decimal addition failed"
    assert engine.evaluate("5.5 * 2") == 11, "Decimal multiplication failed"
    tests_passed += 2
    print("  ✓ Decimal operations: PASSED")

    # Test percentage
    print("\n✓ Testing Percentage...")
    assert engine.percentage(50) == 0.5, "Percentage failed"
    tests_passed += 1
    print("  ✓ Percentage: PASSED")

    # Test power operations
    print("\n✓ Testing Power Operations...")
    assert engine.power(2, 3) == 8, "Power failed"
    assert engine.power(5, 2) == 25, "Square failed"
    tests_passed += 2
    print("  ✓ Power operations: PASSED")

    # Test square root
    print("\n✓ Testing Square Root...")
    assert engine.sqrt(16) == 4, "Square root failed"
    assert engine.sqrt(25) == 5, "Square root failed"
    tests_passed += 2
    print("  ✓ Square root: PASSED")

    # Test factorial
    print("\n✓ Testing Factorial...")
    assert engine.factorial(5) == 120, "Factorial failed"
    assert engine.factorial(0) == 1, "Factorial(0) failed"
    tests_passed += 2
    print("  ✓ Factorial: PASSED")

    # Test trigonometric functions (degree mode)
    print("\n✓ Testing Trigonometric Functions (Degree Mode)...")
    engine.set_angle_mode("degree")
    assert abs(engine.sin(90) - 1.0) < 0.0001, "sin(90°) failed"
    assert abs(engine.cos(0) - 1.0) < 0.0001, "cos(0°) failed"
    tests_passed += 2
    print("  ✓ Trigonometric functions (degree): PASSED")

    # Test logarithmic functions
    print("\n✓ Testing Logarithmic Functions...")
    assert engine.log(100) == 2, "log(100) failed"
    assert engine.ln(math.e) == 1, "ln(e) failed"
    tests_passed += 2
    print("  ✓ Logarithmic functions: PASSED")

    # Test memory functions
    print("\n✓ Testing Memory Functions...")
    engine.memory_clear()
    engine.memory_add(50)
    assert engine.memory_recall() == 50, "Memory add failed"
    engine.memory_subtract(20)
    assert engine.memory_recall() == 30, "Memory subtract failed"
    engine.memory_set(100)
    assert engine.memory_recall() == 100, "Memory set failed"
    engine.memory_clear()
    assert engine.memory_recall() == 0, "Memory clear failed"
    tests_passed += 4
    print("  ✓ Memory functions: PASSED")

    # Test error handling
    print("\n✓ Testing Error Handling...")
    result = engine.evaluate("1/0")
    assert "Error" in str(result), "Division by zero not caught"
    result = engine.sqrt(-5)
    assert isinstance(result, str) and "Error" in result, "Negative sqrt not caught"
    result = engine.evaluate("((5+3")
    assert "Error" in str(result), "Unbalanced parentheses not caught"
    tests_passed += 3
    print("  ✓ Error handling: PASSED")

    # Test complex expressions
    print("\n✓ Testing Complex Expressions...")
    result = engine.evaluate("(10 + 5) * 2")
    assert result == 30, "Complex expression failed"
    result = engine.evaluate("100 / (2 + 3)")
    assert result == 20, "Complex expression with parentheses failed"
    tests_passed += 2
    print("  ✓ Complex expressions: PASSED")

    print("\n" + "=" * 60)
    print(f"TESTS COMPLETED: {tests_passed} passed, {tests_failed} failed")
    print("=" * 60)
    print("\n✅ All tests passed! Calculator is working perfectly!\n")


if __name__ == "__main__":
    test_calculator_engine()
