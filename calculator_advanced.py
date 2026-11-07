"""Tkinter desktop interface for Simple Calculator."""

import math
import re
import tkinter as tk
from tkinter import font, ttk

from calculator_engine import CalculatorEngine


class AdvancedCalculator:
    """Tkinter calculator application with a standard and scientific mode."""

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("620x680")
        self.root.minsize(560, 670)
        self.root.resizable(True, True)

        self.engine = CalculatorEngine()
        self.history = []

        self.display_var = tk.StringVar(value="0")
        self.input_var = tk.StringVar(value="")
        self.scientific_mode = tk.BooleanVar(value=False)

        self.bg_color = "#1e1e1e"
        self.btn_color = "#2d2d2d"
        self.btn_hover = "#3d3d3d"
        self.operator_color = "#ff9500"
        self.accent_color = "#0d7377"
        self.text_color = "#ffffff"
        self.error_color = "#ff6b6b"

        self.root.configure(bg=self.bg_color)

        self.setup_ui()
        self.bind_keys()

    def setup_ui(self):
        """Build the user interface."""
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        display_frame = tk.Frame(main_frame, bg=self.bg_color)
        display_frame.pack(fill=tk.X, pady=(0, 6))

        input_font = font.Font(family="Arial", size=11, weight="normal")
        input_label = tk.Label(
            display_frame,
            textvariable=self.input_var,
            font=input_font,
            bg=self.bg_color,
            fg="#888888",
            anchor="e",
            height=1,
        )
        input_label.pack(fill=tk.X)

        result_font = font.Font(family="Arial", size=18, weight="bold")
        result_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=result_font,
            bg=self.bg_color,
            fg=self.text_color,
            anchor="e",
            height=1,
        )
        result_label.pack(fill=tk.X)

        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=(0, 6))

        self.mode_btn = self.create_button(
            control_frame,
            "Scientific",
            self.toggle_scientific_mode,
            width=11,
            bg=self.accent_color,
            expand=False,
        )

        angle_frame = tk.Frame(control_frame, bg=self.bg_color)
        angle_frame.pack(side=tk.LEFT, padx=5)
        angle_label = tk.Label(
            angle_frame, text="Angle:", bg=self.bg_color, fg=self.text_color
        )
        angle_label.pack(side=tk.LEFT)
        angle_var = tk.StringVar(value="DEG")
        angle_menu = ttk.Combobox(
            angle_frame,
            textvariable=angle_var,
            values=["DEG", "RAD"],
            width=5,
            state="readonly",
        )
        angle_menu.pack(side=tk.LEFT, padx=5)
        angle_menu.bind(
            "<<ComboboxSelected>>", lambda event: self.set_angle_mode(angle_var.get())
        )

        self.create_button(
            control_frame, "(", self.append_value("("), width=3, expand=False
        )
        self.create_button(
            control_frame, ")", self.append_value(")"), width=3, expand=False
        )

        history_frame = tk.Frame(main_frame, bg="#252525", relief=tk.SUNKEN, bd=1)
        history_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 6))

        history_label = tk.Label(
            history_frame,
            text="History",
            font=("Arial", 10, "bold"),
            bg="#252525",
            fg=self.accent_color,
        )
        history_label.pack(anchor="w", padx=5, pady=5)

        scrollbar = ttk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.history_text = tk.Text(
            history_frame,
            height=2,
            width=50,
            bg="#1a1a1a",
            fg="#888888",
            font=("Courier", 8),
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT,
        )
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.history_text.yview)
        self.history_text.config(state=tk.DISABLED)

        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        standard_buttons = [
            ["C", "CE", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "%", "="],
        ]

        for row in standard_buttons:
            row_frame = tk.Frame(buttons_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=3)

            for btn_text in row:
                if btn_text == "=":
                    self.create_button(
                        row_frame,
                        btn_text,
                        self.calculate,
                        bg=self.accent_color,
                    )
                elif btn_text in ["C", "CE", "⌫"]:
                    self.create_button(
                        row_frame,
                        btn_text,
                        self.clear_functions(btn_text),
                        bg=self.error_color,
                    )
                elif btn_text in ["/", "*", "-", "+", "%"]:
                    command = (
                        self.apply_percentage
                        if btn_text == "%"
                        else self.append_operator(btn_text)
                    )
                    self.create_button(
                        row_frame, btn_text, command, bg=self.operator_color
                    )
                else:
                    self.create_button(
                        row_frame, btn_text, self.append_value(btn_text)
                    )

        self.scientific_frame = tk.Frame(buttons_frame, bg=self.bg_color)

        scientific_buttons = [
            ["sin", "cos", "tan", "asin", "acos"],
            ["atan", "log", "ln", "√", "x²"],
            ["x³", "x^y", "!", "π", "e"],
            ["M+", "M-", "MR", "MC", "MS"],
        ]

        for row in scientific_buttons:
            row_frame = tk.Frame(self.scientific_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=2)

            for btn_text in row:
                if btn_text in ["M+", "M-", "MR", "MC", "MS"]:
                    self.create_button(
                        row_frame,
                        btn_text,
                        self.memory_functions(btn_text),
                        bg="#8b4513",
                    )
                else:
                    self.create_button(
                        row_frame,
                        btn_text,
                        self.scientific_operations(btn_text),
                        bg="#6a4c93",
                    )

    def create_button(
        self, parent, text, command, width=7, bg=None, expand=True, height=1
    ):
        """Create a styled calculator button."""
        if bg is None:
            bg = self.btn_color

        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10, "bold"),
            bg=bg,
            fg=self.text_color,
            activebackground=self.btn_hover,
            activeforeground=self.text_color,
            relief=tk.FLAT,
            bd=0,
            width=width,
            height=height,
            cursor="hand2",
        )
        btn.pack(
            side=tk.LEFT,
            expand=expand,
            fill=tk.BOTH if expand else tk.NONE,
            padx=3,
        )
        return btn

    def append_value(self, value):
        """Return a callback that appends a digit, decimal point, or parenthesis."""

        def action():
            current = self.input_var.get()

            if value == "(":
                if current == "0":
                    current = ""
                if current and (current[-1].isdigit() or current[-1] == ")"):
                    current += "*"
                self.input_var.set(current + "(")
            elif value == ")":
                if current.count("(") <= current.count(")"):
                    return
                self.input_var.set(current + ")")
            elif value == ".":
                if self._current_number_has_decimal(current):
                    return
                if current.endswith(")"):
                    current += "*0"
                elif not current or current[-1] in "+-*/%^(":
                    current += "0"
                self.input_var.set(current + ".")
            else:
                if current == "0":
                    current = ""
                if value.isdigit() and current.endswith(")"):
                    current += "*"
                self.input_var.set(current + value)

            self.update_display()

        return action

    @staticmethod
    def _current_number_has_decimal(current):
        """Return True when the number being typed already has a decimal point."""
        tail = re.split(r"[^0-9.]", current)[-1]
        return "." in tail

    def append_operator(self, op):
        """Return a callback that appends or replaces an operator."""

        def action():
            current = self.input_var.get()
            if not current:
                return

            if current[-1] == "(":
                if op != "-":
                    return
                self.input_var.set(current + op)
            elif current[-1] in "+-*/^":
                self.input_var.set(current[:-1] + op)
            elif current[-1] == ".":
                return
            else:
                self.input_var.set(current + op)

            self.update_display()

        return action

    def clear_functions(self, func_type):
        """Return a callback for clear and backspace operations."""

        def action():
            if func_type in ("C", "CE"):
                self.input_var.set("")
                self.display_var.set("0")
            elif func_type == "⌫":
                current = self.input_var.get()
                self.input_var.set(current[:-1] if current else "")
                self.update_display()

        return action

    def calculate(self):
        """Evaluate the expression in the input display."""
        expression = self.input_var.get().strip()
        if not expression:
            return

        result = self.engine.evaluate(expression)
        if isinstance(result, str):
            self.display_var.set(result)
            return

        formatted = self._format_result(result)
        self.display_var.set(formatted)
        self.history.append(f"{expression} = {formatted}")
        self.update_history_display()
        self.input_var.set("")

    @staticmethod
    def _format_result(value):
        """Format results without noisy trailing zeros."""
        if isinstance(value, float):
            if math.isfinite(value) and value.is_integer() and abs(value) < 1e16:
                return str(int(value))
            return f"{value:.12g}"
        return str(value)

    def _current_number(self):
        """Return the numeric value of the current input."""
        text = self.input_var.get().strip()
        if not text:
            return float(self.engine.last_result)

        result = self.engine.evaluate(text)
        if isinstance(result, str):
            raise ValueError(result.removeprefix("Error:").strip())
        return float(result)

    def _set_result(self, result):
        """Show a scientific or memory result in both display lines."""
        self.engine.last_result = float(result)
        formatted = self._format_result(result)
        self.display_var.set(formatted)
        self.input_var.set(formatted)

    def _append_constant(self, constant):
        """Append π or e, inserting multiplication when needed."""
        current = self.input_var.get()
        if current == "0":
            current = ""
        if current and (current[-1].isdigit() or current[-1] == ")"):
            current += "*"
        self.input_var.set(current + str(constant))

    def scientific_operations(self, op):
        """Return a callback for a scientific operation."""

        def action():
            try:
                if op == "π":
                    self._append_constant(math.pi)
                    self.update_display()
                    return
                if op == "e":
                    self._append_constant(math.e)
                    self.update_display()
                    return
                if op == "x^y":
                    current = self.input_var.get()
                    if current and (current[-1].isdigit() or current[-1] == ")"):
                        self.input_var.set(current + "^")
                        self.update_display()
                    return

                value = self._current_number()
                if op == "sin":
                    result = self.engine.sin(value)
                elif op == "cos":
                    result = self.engine.cos(value)
                elif op == "tan":
                    result = self.engine.tan(value)
                elif op == "asin":
                    result = self.engine.asin(value)
                elif op == "acos":
                    result = self.engine.acos(value)
                elif op == "atan":
                    result = self.engine.atan(value)
                elif op == "log":
                    result = self.engine.log(value)
                elif op == "ln":
                    result = self.engine.ln(value)
                elif op == "√":
                    result = self.engine.sqrt(value)
                elif op == "x²":
                    result = self.engine.power(value, 2)
                elif op == "x³":
                    result = self.engine.power(value, 3)
                elif op == "!":
                    result = self.engine.factorial(value)
                else:
                    raise ValueError(f"Unknown operation: {op}")

                self._set_result(result)
            except (ValueError, TypeError, OverflowError) as exc:
                self.display_var.set(f"Error: {exc}")

        return action

    def apply_percentage(self):
        """Convert the current value to a percentage."""
        try:
            self._set_result(self.engine.percentage(self._current_number()))
        except (ValueError, TypeError, OverflowError) as exc:
            self.display_var.set(f"Error: {exc}")

    def memory_functions(self, func):
        """Return a callback for a memory operation."""

        def action():
            try:
                current = self._current_number()

                if func == "M+":
                    self.engine.memory_add(current)
                    self.display_var.set(f"M+ ({self._format_result(self.engine.memory)})")
                elif func == "M-":
                    self.engine.memory_subtract(current)
                    self.display_var.set(f"M- ({self._format_result(self.engine.memory)})")
                elif func == "MR":
                    recall = self.engine.memory_recall()
                    self._set_result(recall)
                elif func == "MC":
                    self.engine.memory_clear()
                    self.display_var.set("Memory cleared")
                elif func == "MS":
                    self.engine.memory_set(current)
                    self.display_var.set(
                        f"Memory set ({self._format_result(current)})"
                    )
            except (ValueError, TypeError, OverflowError) as exc:
                self.display_var.set(f"Error: {exc}")

        return action

    def toggle_scientific_mode(self):
        """Toggle the scientific button panel."""
        self.scientific_mode.set(not self.scientific_mode.get())
        if self.scientific_mode.get():
            self.scientific_frame.pack(fill=tk.BOTH, expand=True, pady=2)
            self.mode_btn.config(text="Standard")
        else:
            self.scientific_frame.pack_forget()
            self.mode_btn.config(text="Scientific")

    def set_angle_mode(self, mode):
        """Set the engine's angle mode from the DEG/RAD selector."""
        self.engine.set_angle_mode("radian" if mode == "RAD" else "degree")

    def update_display(self):
        """Update the result line with a live preview of the input."""
        current = self.input_var.get()
        if not current:
            self.display_var.set("0")
            return

        result = self.engine.evaluate(current)
        if isinstance(result, str):
            self.display_var.set(current)
        else:
            self.display_var.set(f"= {self._format_result(result)}")

    def update_history_display(self):
        """Refresh the visible history panel."""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for item in self.history[-10:]:
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state=tk.DISABLED)

    def bind_keys(self):
        """Bind keyboard events."""
        self.root.bind("<0>", lambda event: self.append_value("0")())
        self.root.bind("<1>", lambda event: self.append_value("1")())
        self.root.bind("<2>", lambda event: self.append_value("2")())
        self.root.bind("<3>", lambda event: self.append_value("3")())
        self.root.bind("<4>", lambda event: self.append_value("4")())
        self.root.bind("<5>", lambda event: self.append_value("5")())
        self.root.bind("<6>", lambda event: self.append_value("6")())
        self.root.bind("<7>", lambda event: self.append_value("7")())
        self.root.bind("<8>", lambda event: self.append_value("8")())
        self.root.bind("<9>", lambda event: self.append_value("9")())
        self.root.bind("<plus>", lambda event: self.append_operator("+")())
        self.root.bind("<minus>", lambda event: self.append_operator("-")())
        self.root.bind("<asterisk>", lambda event: self.append_operator("*")())
        self.root.bind("<slash>", lambda event: self.append_operator("/")())
        self.root.bind("<period>", lambda event: self.append_value(".")())
        self.root.bind("<parenleft>", lambda event: self.append_value("(")())
        self.root.bind("<parenright>", lambda event: self.append_value(")")())
        self.root.bind("<asciicircum>", lambda event: self.append_operator("^")())
        self.root.bind("<percent>", lambda event: self.apply_percentage())
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.clear_functions("⌫")())
        self.root.bind("<Escape>", lambda event: self.clear_functions("C")())


def main():
    """Main entry point."""
    root = tk.Tk()
    AdvancedCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
