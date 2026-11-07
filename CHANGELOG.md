# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-11-07

### Added

- MIT `LICENSE` file matching the license declared in the original README.
- `CONTRIBUTING.md`, `SECURITY.md`, this changelog, issue forms, and a pull
  request template.
- GitHub Actions CI for linting, tests, and a Linux GUI smoke test.
- Dependabot configuration for pip and GitHub Actions.
- Standard-library test suite covering the engine, CLI, and GUI.
- Real screenshots, an animated demo GIF, and a social preview asset.
- `run.py` convenience launcher with `gui`, `cli`, `test`, and `check`
  commands.
- `pyproject.toml` Ruff configuration, `requirements-dev.txt`, `.editorconfig`,
  and `.gitattributes`.

### Changed

- Rewrote the README for the actual repository, including verified install
  commands, real screenshots, accurate requirements, limitations, and working
  links.
- Replaced the `eval`-based expression path with an AST whitelist evaluator.
- Reduced the GUI footprint for small and high-DPI displays; added parentheses
  buttons, a percentage button, and responsive resizing.
- Improved GUI error handling and result formatting.
- Made `requirements.txt` valid for `pip install -r requirements.txt`.
- Expanded `.gitignore` for tests, tooling, local environments, and build
  output.

### Fixed

- Factorial failed for integer-valued floats entered through the GUI.
- The `x^y` button produced an operator the engine rejected.
- Percentage was documented but unavailable in the GUI.
- Tests crashed on Windows consoles that use the cp1252 encoding.
- Memory operations could fail after the live preview displayed `= result`.
- README links pointed to a different repository, and the clone command used
  the wrong project name.
- The README referenced a `LICENSE` file that did not exist.
- `pip install -r requirements.txt` failed because of an invalid
  `Python>=3.6` requirement line.
- The fixed-size GUI clipped buttons on high-DPI displays.

### Removed

- `setup.py` (replaced by `run.py`; it was a launcher, not a packaging file).
- `FEATURES.md` (duplicated the README and contained unverified claims).
- `MAKE_PUBLIC.md` (the repository is already public; the file included an
  insecure token example).

[Unreleased]: https://github.com/ShahabAhmed01/simple-calculator/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ShahabAhmed01/simple-calculator/releases/tag/v0.1.0
