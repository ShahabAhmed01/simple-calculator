"""Capture real screenshots and a demo GIF from the Tkinter application.

This is an optional Windows-only developer tool. It uses Pillow's ImageGrab,
so install Pillow in a separate environment before running it:

    python -m pip install pillow
    python tools/capture_demo.py

The script writes:

    docs/images/calculator.png
    docs/images/calculator-scientific.png
    docs/images/demo.gif
"""

import ctypes
import platform
import sys
import time
import tkinter as tk
from ctypes import wintypes
from pathlib import Path

try:
    from PIL import Image, ImageGrab
except ImportError:  # pragma: no cover - optional tooling
    print("This script requires Pillow. Install it with: python -m pip install pillow")
    raise SystemExit(1) from None

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "images"
WINDOW = "620x680+80+40"


def make_dpi_aware():
    """Make screenshot coordinates match physical pixels on Windows."""
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def client_bbox(root):
    """Return the screen-space bounding box of a Tk window's client area."""
    hwnd = ctypes.windll.user32.GetAncestor(root.winfo_id(), 2)  # GA_ROOT
    rect = wintypes.RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(rect))
    point = wintypes.POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(point))
    return (point.x, point.y, point.x + rect.right, point.y + rect.bottom)


def settle(root, seconds=0.35):
    """Process pending Tk events and give the compositor time to redraw."""
    root.update()
    time.sleep(seconds)
    root.update()


def show_window(root):
    root.geometry(WINDOW)
    root.deiconify()
    root.lift()
    root.attributes("-topmost", True)
    root.focus_force()
    settle(root, 0.8)


def grab(root):
    return ImageGrab.grab(bbox=client_bbox(root), all_screens=True)


def create_app():
    root = tk.Tk()
    from calculator_advanced import AdvancedCalculator

    app = AdvancedCalculator(root)
    show_window(root)
    return root, app


def type_values(app, values):
    for value in values:
        app.append_value(value)()


def standard_screenshot():
    root, app = create_app()
    type_values(app, "12")
    app.append_operator("+")()
    type_values(app, "30")
    app.calculate()
    app.input_var.set("12+30")
    app.update_display()
    settle(root)
    image = grab(root)
    image.save(IMAGES / "calculator.png")
    root.destroy()
    return image


def scientific_screenshot():
    root, app = create_app()
    type_values(app, "45")
    app.append_operator("+")()
    type_values(app, "45")
    app.calculate()
    app.toggle_scientific_mode()
    app.input_var.set("90")
    app.scientific_operations("sin")()
    app.input_var.set("90")
    settle(root)
    image = grab(root)
    image.save(IMAGES / "calculator-scientific.png")
    root.destroy()
    return image


def demo_gif():
    root, app = create_app()
    frames = []

    def capture():
        settle(root, 0.45)
        frames.append(grab(root).convert("RGB"))

    capture()
    type_values(app, "1")
    capture()
    type_values(app, "2")
    capture()
    app.append_operator("+")()
    capture()
    type_values(app, "3")
    capture()
    type_values(app, "0")
    capture()
    app.calculate()
    capture()
    app.toggle_scientific_mode()
    capture()
    app.clear_functions("C")()
    type_values(app, "9")
    capture()
    app.scientific_operations("!")()
    capture()
    app.clear_functions("C")()
    type_values(app, "90")
    capture()
    app.scientific_operations("sin")()
    app.input_var.set("90")
    capture()

    root.destroy()

    palette_frames = [
        frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
        for frame in frames
    ]
    durations = [450] * (len(palette_frames) - 1) + [1500]
    output = IMAGES / "demo.gif"
    palette_frames[0].save(
        output,
        save_all=True,
        append_images=palette_frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2,
    )
    return output


def main():
    if platform.system() != "Windows":
        print("This capture tool currently supports Windows only.")
        return 1

    make_dpi_aware()
    IMAGES.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(ROOT))

    standard = standard_screenshot()
    print(f"Saved {IMAGES / 'calculator.png'} ({standard.size[0]}x{standard.size[1]})")

    scientific = scientific_screenshot()
    print(
        f"Saved {IMAGES / 'calculator-scientific.png'} "
        f"({scientific.size[0]}x{scientific.size[1]})"
    )

    gif = demo_gif()
    print(f"Saved {gif} ({gif.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
