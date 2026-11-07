"""Compatibility test entry point.

Prefer the standard-library discover command:

    python -m unittest discover -s tests -t . -v

or the convenience runner:

    python run.py test
"""

import unittest


def main():
    suite = unittest.defaultTestLoader.discover("tests", top_level_dir=".")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
