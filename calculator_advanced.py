"""
Advanced Calculator with GUI
A feature-rich calculator with scientific functions, history, and memory.
Built with Tkinter for cross-platform compatibility.
"""

import tkinter as tk
from tkinter import font, messagebox
import tkinter.ttk as ttk
from calculator_engine import CalculatorEngine
import math


class AdvancedCalculator:
    """Advanced Calculator GUI Application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        # Initialize engine
        self.engine = CalculatorEngine()

        # Display variables
        self.display_var = tk.StringVar(value="0")
        self.input_var = tk.StringVar(value="")
        self.scientific_mode = tk.BooleanVar(value=False)

        # Colors
        self.bg_color = "#1e1e1e"
        self.btn_color = "#2d2d2d"
        self.btn_hover = "#3d3d3d"
        self.operator_color = "#ff9500"
        self.accent_color = "#0d7377"
        self.text_color = "#ffffff"
        self.error_color = "#ff6b6b"

        self.root.configure(bg=self.bg_color)

        # Build UI
        self.setup_ui()
        self.bind_keys()

        # History
        self.history = []

    def setup_ui(self):
        """Build the user interface."""

        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Display frame
        display_frame = tk.Frame(main_frame, bg=self.bg_color)
        display_frame.pack(fill=tk.X, pady=(0, 10))

        # Input display
        input_font = font.Font(family="Arial", size=14, weight="normal")
        input_label = tk.Label(
            display_frame, textvariable=self.input_var, font=input_font,
            bg=self.bg_color, fg="#888888", anchor="e", height=1
        )
        input_label.pack(fill=tk.X)

        # Result display
        result_font = font.Font(family="Arial", size=24, weight="bold")
        result_label = tk.Label(
            display_frame, textvariable=self.display_var, font=result_font,
            bg=self.bg_color, fg=self.text_color, anchor="e", height=2
        )
        result_label.pack(fill=tk.X)

        # Control bar
        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=(0, 10))

        # Mode toggle
        mode_btn = self.create_button(
            control_frame, "Scientific", self.toggle_scientific_mode,
            width=12, bg=self.accent_color
        )
        mode_btn.pack(side=tk.LEFT, padx=5)

        # Angle mode
        angle_frame = tk.Frame(control_frame, bg=self.bg_color)
        angle_frame.pack(side=tk.LEFT, padx=5)
        angle_label = tk.Label(angle_frame, text="Angle:", bg=self.bg_color, fg=self.text_color)
        angle_label.pack(side=tk.LEFT)
        angle_var = tk.StringVar(value="DEG")
        angle_menu = ttk.Combobox(
            angle_frame, textvariable=angle_var, values=["DEG", "RAD"],
            width=5, state="readonly"
        )
        angle_menu.pack(side=tk.LEFT, padx=5)
        angle_menu.bind("<<ComboboxSelected>>", lambda e: self.set_angle_mode(angle_var.get()))

        # History frame (right side)
        history_frame = tk.Frame(main_frame, bg="#252525", relief=tk.SUNKEN, bd=1)
        history_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        history_label = tk.Label(
            history_frame, text="History", font=("Arial", 10, "bold"),
            bg="#252525", fg=self.accent_color
        )
        history_label.pack(anchor="w", padx=5, pady=5)

        # Scrollable history
        scrollbar = ttk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.history_text = tk.Text(
            history_frame, height=6, width=50, bg="#1a1a1a",
            fg="#888888", font=("Courier", 9),
            yscrollcommand=scrollbar.set, relief=tk.FLAT
        )
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.history_text.yview)
        self.history_text.config(state=tk.DISABLED)

        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        # Standard buttons
        standard_buttons = [
            ["C", "CE", "⌫", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""],
        ]

        for row in standard_buttons:
            row_frame = tk.Frame(buttons_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=5)

            for btn_text in row:
                if btn_text == "":
                    continue
                elif btn_text == "=":
                    self.create_button(row_frame, btn_text, self.calculate, width=7, bg=self.accent_color)
                elif btn_text in ["C", "CE", "⌫"]:
                    self.create_button(row_frame, btn_text, self.clear_functions(btn_text), width=7, bg=self.error_color)
                elif btn_text in ["/", "*", "-", "+"]:
                    self.create_button(row_frame, btn_text, self.append_operator(btn_text), width=7, bg=self.operator_color)
                else:
                    self.create_button(row_frame, btn_text, self.append_value(btn_text), width=7)

        # Scientific buttons
        self.scientific_frame = tk.Frame(buttons_frame, bg=self.bg_color)

        scientific_buttons = [
            ["sin", "cos", "tan", "π"],
            ["asin", "acos", "atan", "e"],
            ["log", "ln", "√", "x²"],
            ["x³", "x^y", "!", "M+"],
            ["M-", "MR", "MC", "MS"],
        ]

        for row in scientific_buttons:
            row_frame = tk.Frame(self.scientific_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.BOTH, expand=True, pady=3)

            for btn_text in row:
                if btn_text in ["M+", "M-", "MR", "MC", "MS"]:
                    self.create_button(row_frame, btn_text, self.memory_functions(btn_text), width=7, bg="#8b4513")
                else:
                    self.create_button(row_frame, btn_text, self.scientific_operations(btn_text), width=7, bg="#6a4c93")

    def create_button(self, parent, text, command, width=7, bg=None):
        """Create a styled button."""
        if bg is None:
            bg = self.btn_color

        btn = tk.Button(
            parent, text=text, command=command, font=("Arial", 12, "bold"),
            bg=bg, fg=self.text_color, activebackground=self.btn_hover,
            activeforeground=self.text_color, relief=tk.FLAT, bd=0,
            width=width, height=2, cursor="hand2"
        )
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=3)
        return btn

    def append_value(self, value):
        """Return function to append value to input."""
        def action():
            current = self.input_var.get()
            if current == "0":
                self.input_var.set(value)
            else:
                self.input_var.set(current + value)
            self.update_display()
        return action

    def append_operator(self, op):
        """Return function to append operator."""
        def action():
            current = self.input_var.get()
            if current and not current[-1] in "+-*/.":
                self.input_var.set(current + op)
        return action

    def clear_functions(self, func_type):
        """Return function for clear operations."""
        def action():
            if func_type == "C":
                self.input_var.set("")
                self.display_var.set("0")
            elif func_type == "CE":
                self.input_var.set("")
                self.update_display()
            elif func_type == "⌫":
                current = self.input_var.get()
                self.input_var.set(current[:-1] if current else "")
                self.update_display()
        return action

    def calculate(self):
        """Evaluate the expression."""
        expression = self.input_var.get()
        if not expression:
            return

        result = self.engine.evaluate(expression)

        if isinstance(result, str) and result.startswith("Error"):
            self.display_var.set(result)
        else:
            self.display_var.set(str(result))
            self.history.append(f"{expression} = {result}")
            self.update_history_display()
            self.input_var.set("")

    def scientific_operations(self, op):
        """Return function for scientific operations."""
        def action():
            current = self.input_var.get()
            result = None

            try:
                if op == "sin":
                    result = self.engine.sin(float(current) if current else 0)
                elif op == "cos":
                    result = self.engine.cos(float(current) if current else 0)
                elif op == "tan":
                    result = self.engine.tan(float(current) if current else 0)
                elif op == "asin":
                    result = self.engine.asin(float(current) if current else 0)
                elif op == "acos":
                    result = self.engine.acos(float(current) if current else 0)
                elif op == "atan":
                    result = self.engine.atan(float(current) if current else 0)
                elif op == "log":
                    result = self.engine.log(float(current) if current else 0)
                elif op == "ln":
                    result = self.engine.ln(float(current) if current else 0)
                elif op == "√":
                    result = self.engine.sqrt(float(current) if current else 0)
                elif op == "x²":
                    result = (float(current) if current else 0) ** 2
                elif op == "x³":
                    result = (float(current) if current else 0) ** 3
                elif op == "!":
                    result = self.engine.factorial(float(current) if current else 0)
                elif op == "π":
                    self.input_var.set((current if current else "") + str(math.pi))
                    return
                elif op == "e":
                    self.input_var.set((current if current else "") + str(math.e))
                    return
                elif op == "x^y":
                    self.input_var.set((current if current else "") + "^")
                    return

                if result is not None:
                    self.display_var.set(str(result))
                    self.input_var.set(str(result))

            except ValueError as e:
                self.display_var.set(f"Error: {str(e)}")

        return action

    def memory_functions(self, func):
        """Handle memory operations."""
        def action():
            try:
                current = float(self.display_var.get()) if self.display_var.get() and not self.display_var.get().startswith("Error") else 0

                if func == "M+":
                    self.engine.memory_add(current)
                    self.display_var.set(f"M+ ({self.engine.memory})")
                elif func == "M-":
                    self.engine.memory_subtract(current)
                    self.display_var.set(f"M- ({self.engine.memory})")
                elif func == "MR":
                    recall = self.engine.memory_recall()
                    self.display_var.set(str(recall))
                    self.input_var.set(str(recall))
                elif func == "MC":
                    self.engine.memory_clear()
                    self.display_var.set("Memory Cleared")
                elif func == "MS":
                    self.engine.memory_set(current)
                    self.display_var.set(f"Memory Set ({current})")
            except Exception as e:
                self.display_var.set(f"Error: {str(e)}")

        return action

    def toggle_scientific_mode(self):
        """Toggle scientific mode."""
        self.scientific_mode.set(not self.scientific_mode.get())
        if self.scientific_mode.get():
            self.scientific_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        else:
            self.scientific_frame.pack_forget()

    def set_angle_mode(self, mode):
        """Set angle mode."""
        self.engine.set_angle_mode("radian" if mode == "RAD" else "degree")

    def update_display(self):
        """Update display with current input."""
        current = self.input_var.get()
        if current:
            try:
                result = self.engine.evaluate(current)
                if not isinstance(result, str):
                    self.display_var.set(f"= {result}")
                else:
                    self.display_var.set(current)
            except:
                self.display_var.set(current)
        else:
            self.display_var.set("0")

    def update_history_display(self):
        """Update history panel."""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for item in self.history[-10:]:  # Show last 10 items
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.config(state=tk.DISABLED)

    def bind_keys(self):
        """Bind keyboard events."""
        self.root.bind("<0>", lambda e: self.append_value("0")())
        self.root.bind("<1>", lambda e: self.append_value("1")())
        self.root.bind("<2>", lambda e: self.append_value("2")())
        self.root.bind("<3>", lambda e: self.append_value("3")())
        self.root.bind("<4>", lambda e: self.append_value("4")())
        self.root.bind("<5>", lambda e: self.append_value("5")())
        self.root.bind("<6>", lambda e: self.append_value("6")())
        self.root.bind("<7>", lambda e: self.append_value("7")())
        self.root.bind("<8>", lambda e: self.append_value("8")())
        self.root.bind("<9>", lambda e: self.append_value("9")())
        self.root.bind("<plus>", lambda e: self.append_operator("+")())
        self.root.bind("<minus>", lambda e: self.append_operator("-")())
        self.root.bind("<asterisk>", lambda e: self.append_operator("*")())
        self.root.bind("<slash>", lambda e: self.append_operator("/")())
        self.root.bind("<period>", lambda e: self.append_value(".")())
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<BackSpace>", lambda e: self.clear_functions("⌫")())
        self.root.bind("<Escape>", lambda e: self.clear_functions("C")())


def main():
    """Main entry point."""
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
