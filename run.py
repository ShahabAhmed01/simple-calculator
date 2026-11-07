#!/usr/bin/env python3
"""Convenience launcher for Simple Calculator.

Usage:
    python run.py          Show an interactive menu
    python run.py gui      Launch the Tkinter calculator
    python run.py cli      Launch the command-line calculator
    python run.py test     Run the test suite
    python run.py check    Check the Python and Tkinter installation
"""

import platform
import subprocess
import sys
from importlib.util import find_spec


def check_python_version() -> bool:
    """Require Python 3.10 or newer."""
    if sys.version_info < (3, 10):  # noqa: UP036 - user-facing runtime check
        print("Error: Python 3.10 or newer is required.")
        print(f"Current version: {sys.version.split()[0]}")
        return False
    print(f"Python version: {sys.version.split()[0]}")
    return True


def check_tkinter() -> bool:
    """Check whether Tkinter is installed."""
    if find_spec("tkinter") is not None:
        print("Tkinter is available.")
        return True

    print("Tkinter is not available.")
    system = platform.system()
    if system == "Windows":
        print("Reinstall Python from python.org and enable the Tcl/Tk option.")
    elif system == "Darwin":
        print("Install Python from python.org, or use: brew install python-tk")
    else:
        print("Ubuntu/Debian: sudo apt-get install python3-tk")
        print("Fedora: sudo dnf install python3-tkinter")
        print("Arch Linux: sudo pacman -S tk")
    return False


def run_tests() -> bool:
    """Run the standard-library test suite."""
    print("Running tests...")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", ".", "-v"],
        check=False,
    )
    if result.returncode == 0:
        print("All tests passed.")
        return True
    print("Tests failed.")
    return False


def run_gui() -> None:
    """Launch the Tkinter application."""
    if not check_tkinter():
        return
    print("Starting Simple Calculator...")
    subprocess.run([sys.executable, "calculator_advanced.py"], check=False)


def run_cli() -> None:
    """Launch the command-line calculator."""
    print("Starting the command-line calculator...")
    subprocess.run([sys.executable, "calculator.py"], check=False)


def interactive_menu() -> None:
    """Ask the user which entry point to run."""
    print("\nSimple Calculator")
    print("1. Launch the GUI calculator")
    print("2. Launch the command-line calculator")
    print("3. Run tests")
    print("4. Check the installation")
    print("5. Exit")

    choice = input("\nEnter choice (1/2/3/4/5): ").strip()
    if choice == "1":
        run_gui()
    elif choice == "2":
        run_cli()
    elif choice == "3":
        run_tests()
    elif choice == "4":
        check_python_version()
        check_tkinter()
    elif choice == "5":
        print("Exiting.")
    else:
        print("Invalid choice.")


def main() -> int:
    """Run a command from the command line or show the interactive menu."""
    print("=" * 50)
    print("Simple Calculator")
    print("=" * 50)

    if not check_python_version():
        return 1

    if len(sys.argv) == 1:
        interactive_menu()
        return 0

    command = sys.argv[1].lower()
    if command == "gui":
        run_gui()
    elif command == "cli":
        run_cli()
    elif command == "test":
        return 0 if run_tests() else 1
    elif command == "check":
        return 0 if check_tkinter() else 1
    else:
        print(f"Unknown command: {command}")
        print("Available commands: gui, cli, test, check")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
