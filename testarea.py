#!/usr/bin/env python3
"""Simple TextArea App."""

from textual.app import ComposeResult, App
from textual.widgets import TextArea, Button, Header
from textual.containers import Vertical
from lorem_text import lorem

LOREM = lorem.paragraphs(13)


class SimpleTextAreaApp(App):
    """Simple app with TextArea and exit button."""

    THEME = "dracula"  # Anderes Theme probieren

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield TextArea(text=LOREM, id="textarea")
            yield Button("Exit", id="exit", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit":
            self.exit()


if __name__ == "__main__":
    app = SimpleTextAreaApp()
    app.run()
