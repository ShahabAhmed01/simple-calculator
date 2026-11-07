"""Tests for the Tkinter interface.

The tests are skipped automatically when Tkinter or a display server is not
available, which keeps the engine tests runnable in headless environments.
"""

import unittest

try:
    import tkinter as tk
except ImportError:  # pragma: no cover - platform dependent
    tk = None

if tk is None:  # pragma: no cover - platform dependent
    AdvancedCalculator = None
else:
    from calculator_advanced import AdvancedCalculator


@unittest.skipIf(tk is None, "Tkinter is not available")
class CalculatorGuiTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:  # pragma: no cover - headless CI
            self.skipTest(f"Tk display is not available: {exc}")

        self.root.withdraw()
        self.app = AdvancedCalculator(self.root)
        self.root.update_idletasks()

    def tearDown(self):
        self.root.destroy()

    def test_basic_calculation_and_history(self):
        for value in "12":
            self.app.append_value(value)()
        self.app.append_operator("+")()
        for value in "30":
            self.app.append_value(value)()

        self.app.calculate()

        self.assertEqual(self.app.display_var.get(), "42")
        self.assertEqual(self.app.history, ["12+30 = 42"])

    def test_live_preview(self):
        self.app.input_var.set("2+3")
        self.app.update_display()
        self.assertEqual(self.app.display_var.get(), "= 5")

    def test_decimal_calculation(self):
        self.app.input_var.set("1.5")
        self.app.append_operator("+")()
        self.app.input_var.set(self.app.input_var.get() + "2.5")
        self.app.calculate()
        self.assertEqual(self.app.display_var.get(), "4")

    def test_parentheses_and_power(self):
        self.app.input_var.set("(2+3)*2")
        self.app.calculate()
        self.assertEqual(self.app.display_var.get(), "10")

        self.app.input_var.set("2^10")
        self.app.calculate()
        self.assertEqual(self.app.display_var.get(), "1024")

    def test_parenthesis_buttons(self):
        self.app.input_var.set("0")
        self.app.append_value("(")()
        self.assertEqual(self.app.input_var.get(), "(")

        self.app.clear_functions("C")()
        self.app.append_value("5")()
        self.app.append_value("(")()
        self.assertEqual(self.app.input_var.get(), "5*(")

    def test_scientific_factorial_accepts_float_input(self):
        self.app.input_var.set("5")
        self.app.scientific_operations("!")()
        self.assertEqual(self.app.display_var.get(), "120")

    def test_percentage_button(self):
        self.app.input_var.set("50")
        self.app.apply_percentage()
        self.assertEqual(self.app.display_var.get(), "0.5")
        self.assertEqual(self.app.input_var.get(), "0.5")

    def test_memory_round_trip(self):
        self.app.input_var.set("50+30")
        self.app.calculate()

        self.app.memory_functions("M+")()
        self.assertEqual(self.app.engine.memory, 80)

        self.app.memory_functions("MR")()
        self.assertEqual(self.app.input_var.get(), "80")

        self.app.memory_functions("MC")()
        self.assertEqual(self.app.engine.memory, 0)

    def test_error_is_displayed(self):
        self.app.input_var.set("1/0")
        self.app.calculate()
        self.assertEqual(self.app.display_var.get(), "Error: Division by zero")

    def test_scientific_panel_toggle(self):
        self.assertFalse(self.app.scientific_mode.get())
        self.app.toggle_scientific_mode()
        self.assertTrue(self.app.scientific_mode.get())
        self.assertEqual(self.app.scientific_frame.winfo_manager(), "pack")
        self.app.toggle_scientific_mode()
        self.assertEqual(self.app.scientific_frame.winfo_manager(), "")


if __name__ == "__main__":
    unittest.main()
