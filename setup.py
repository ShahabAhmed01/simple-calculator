#!/usr/bin/env python3
"""
Advanced Calculator - Setup and Deployment Script
This script helps set up and run the Advanced Calculator application.
"""

import os
import sys
import subprocess
import platform


def check_python_version():
    """Check if Python version is 3.6 or higher."""
    if sys.version_info < (3, 6):
        print("❌ Error: Python 3.6 or higher is required.")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python version: {sys.version.split()[0]}")


def check_tkinter():
    """Check if Tkinter is available."""
    try:
        import tkinter
        print("✓ Tkinter is available")
        return True
    except ImportError:
        print("❌ Tkinter is not available!")
        print("\nTo install Tkinter:")
        
        system = platform.system()
        if system == "Windows":
            print("  Download Python from python.org and include Tkinter in the installation")
        elif system == "Darwin":  # macOS
            print("  Tkinter should be included with Python from python.org")
            print("  If using Homebrew: brew install python-tk@3.9")
        else:  # Linux
            print("  Ubuntu/Debian: sudo apt-get install python3-tk")
            print("  Fedora: sudo dnf install python3-tkinter")
            print("  Arch: sudo pacman -S tk")
        return False


def run_tests():
    """Run the calculator test suite."""
    print("\n" + "=" * 60)
    print("Running Tests...")
    print("=" * 60)
    try:
        result = subprocess.run([sys.executable, "test_calculator.py"], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed with return code {e.returncode}")
        return False


def run_calculator():
    """Run the advanced calculator."""
    print("\n" + "=" * 60)
    print("Starting Advanced Calculator...")
    print("=" * 60)
    try:
        subprocess.run([sys.executable, "calculator_advanced.py"], check=True)
    except KeyboardInterrupt:
        print("\n\nCalculator closed by user.")
    except Exception as e:
        print(f"❌ Error running calculator: {e}")


def main():
    """Main setup function."""
    print("\n" + "=" * 60)
    print("Advanced Calculator - Setup")
    print("=" * 60 + "\n")

    # Check Python version
    check_python_version()

    # Check Tkinter
    if not check_tkinter():
        sys.exit(1)

    print("\n" + "-" * 60)
    print("Available Commands:")
    print("-" * 60)
    print("  python setup.py test      - Run test suite")
    print("  python setup.py run       - Run the calculator")
    print("  python calculator_advanced.py - Run directly")
    print("  python calculator.py      - Run simple CLI calculator")
    print("-" * 60)

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "test":
            if run_tests():
                print("\n✅ All tests passed! Calculator is ready to use.")
        elif command == "run":
            run_calculator()
        else:
            print(f"Unknown command: {command}")
    else:
        # Ask user
        print("\nWhat would you like to do?")
        print("1. Run tests")
        print("2. Run calculator")
        print("3. Exit")
        
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == "1":
            run_tests()
        elif choice == "2":
            run_calculator()
        else:
            print("Exiting...")


if __name__ == "__main__":
    main()
