"""Build the 1280x640 social preview from the real application screenshot.

Run after tools/capture_demo.py:

    python -m pip install pillow
    python tools/make_social_preview.py

The editable source is this script; the generated asset is
docs/social-preview.png.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT = ROOT / "docs" / "images" / "calculator.png"
OUTPUT = ROOT / "docs" / "social-preview.png"

BACKGROUND = "#17191b"
PANEL = "#202326"
WHITE = "#f5f7f7"
MUTED = "#9aa4a6"
ACCENT = "#14b8a6"
ORANGE = "#ff9500"


def load_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def rounded_screenshot(path, height):
    image = Image.open(path).convert("RGB")
    width = round(image.width * height / image.height)
    image = image.resize((width, height), Image.Resampling.LANCZOS)
    return image


def main():
    if not SCREENSHOT.exists():
        raise SystemExit(f"Missing screenshot: {SCREENSHOT}")

    canvas = Image.new("RGB", (1280, 640), BACKGROUND)
    draw = ImageDraw.Draw(canvas)

    # Subtle panel and accent details.
    draw.rounded_rectangle((40, 40, 700, 600), radius=24, fill=PANEL)
    draw.rounded_rectangle((40, 40, 700, 48), radius=4, fill=ACCENT)
    draw.ellipse((78, 96, 94, 112), fill=ORANGE)

    title_font = load_font(58, bold=True)
    subtitle_font = load_font(26)
    body_font = load_font(22)
    small_font = load_font(18)

    draw.text((80, 140), "Simple Calculator", font=title_font, fill=WHITE)
    draw.text(
        (80, 220),
        "Python + Tkinter desktop calculator",
        font=subtitle_font,
        fill=ACCENT,
    )

    bullets = [
        "Scientific functions and DEG/RAD modes",
        "Memory, history, and keyboard support",
        "No third-party runtime dependencies",
    ]
    y = 292
    for bullet in bullets:
        draw.ellipse((82, y + 8, 92, y + 18), fill=ORANGE)
        draw.text((108, y), bullet, font=body_font, fill=MUTED)
        y += 48

    draw.text(
        (80, 530),
        "github.com/ShahabAhmed01/simple-calculator",
        font=small_font,
        fill=MUTED,
    )

    screenshot = rounded_screenshot(SCREENSHOT, 540)
    x = 760
    y = 50
    draw.rounded_rectangle(
        (x - 8, y - 8, x + screenshot.width + 8, y + screenshot.height + 8),
        radius=16,
        fill="#2b3033",
    )
    canvas.paste(screenshot, (x, y))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, optimize=True)
    print(f"Saved {OUTPUT} ({OUTPUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
