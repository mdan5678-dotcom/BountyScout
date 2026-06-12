"""
Bounty Hunter smoke and regression tests.

These tests avoid external network calls and validate local formatting behavior.
"""

from pathlib import Path

from scout_bounties import format_opportunity_word


def test_repository_has_python_files():
    root = Path(__file__).resolve().parents[1]
    py_files = list(root.glob("*.py")) + list(root.glob("**/*.py"))
    py_files = [p for p in py_files if ".venv" not in str(p) and "site-packages" not in str(p)]
    assert py_files, "Expected at least one Python file in the repository"


def test_opportunity_word_pluralization():
    assert format_opportunity_word(1) == "opportunity"
    assert format_opportunity_word(2) == "opportunities"
    assert format_opportunity_word(12, capitalize=True) == "Opportunities"
