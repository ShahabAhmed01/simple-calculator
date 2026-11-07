# Contributing to Simple Calculator

Thanks for taking the time to contribute. This is a small educational project,
so focused changes and clear bug reports are especially useful.

## Before you start

- Search existing issues and pull requests before opening a new one.
- For security problems, follow [SECURITY.md](SECURITY.md) instead of opening
  a public issue.
- Keep the runtime dependency-free. The calculator uses only the Python
  standard library, including Tkinter.

## Development setup

Requirements: Python 3.10+ and Tkinter.

```bash
git clone https://github.com/ShahabAhmed01/simple-calculator.git
cd simple-calculator

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

python -m pip install -r requirements-dev.txt
```

Run the application:

```bash
python calculator_advanced.py   # desktop GUI
python calculator.py            # command-line mode
python run.py                   # menu
```

## Tests and linting

Run the full test suite:

```bash
python -m unittest discover -s tests -t . -v
```

Run the linter:

```bash
python -m ruff check .
```

GUI tests are skipped automatically when Tkinter or a display server is not
available. If you change the GUI, test it on a machine with a display when
possible, and describe what you tested in the pull request.

## What to work on

Good contributions include:

- Reproducible bug fixes with a regression test
- New tests for untested behavior
- Documentation corrections
- Small usability improvements to the GUI or CLI
- Accessibility and keyboard-navigation improvements

Please avoid large refactors, new runtime dependencies, or unrelated formatting
changes in the same pull request. If a change is large, open an issue first so
the approach can be discussed.

## Pull requests

1. Fork the repository and create a branch from `main`.
2. Use a descriptive branch name, such as `fix/factorial-float` or
   `docs/tkinter-setup`.
3. Keep the change focused and add or update tests.
4. Update the README or CHANGELOG when user-facing behavior changes.
5. Run the tests and linter before opening the pull request.
6. Open a pull request using the template and describe the verification you
   performed.

### Commit messages

Write short, imperative commit messages. Examples:

```text
Fix factorial for integer-valued floats
Add GUI regression tests
Document Linux Tkinter setup
```

### Code style

- Follow PEP 8 and keep lines readable.
- Use type hints where they clarify public behavior.
- Keep the engine independent of Tkinter so it remains testable.
- Add docstrings for new public functions or non-obvious behavior.
- Do not weaken or delete tests to make a change pass.

## Bug reports

Use the bug report template and include:

- Operating system and Python version
- The exact action or expression that failed
- What you expected and what happened
- A screenshot or short recording for GUI problems
- Relevant error output with secrets or personal data removed

## Feature requests

Use the feature request template. Explain the problem first, then the proposed
solution and any alternatives. Features that keep the app small, local, and
dependency-free are the easiest to accept.

## Code of conduct

Be respectful and constructive. Harassment, personal attacks, and
discriminatory behavior are not welcome. Maintainers may close or remove
content that violates these expectations.
