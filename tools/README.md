# Developer asset tools

These scripts regenerate the visual assets in `docs/`. They are not needed to
run the calculator and are not installed by the app.

Requirements: Python 3.10+ and [Pillow](https://python-pillow.org/), on Windows.

```bash
python -m pip install pillow
python tools/capture_demo.py
python tools/make_social_preview.py
```

`capture_demo.py` opens the real Tkinter application, performs real button
actions, and captures the window. It writes:

- `docs/images/calculator.png`
- `docs/images/calculator-scientific.png`
- `docs/images/demo.gif`

`make_social_preview.py` composes the 1280x640 social preview at
`docs/social-preview.png` from the real screenshot.

Do not replace these images with mockups or stock images.
