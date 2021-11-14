#!/usr/bin/env python3

"""
This example demonstrates a simple text highlighter.
"""

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "strike bright_green"})
console = Console(highlighter=EmailHighlighter(), theme=theme)

console.print("Send funds to money@example.org")
