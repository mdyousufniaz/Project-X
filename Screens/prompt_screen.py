from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Grid

class PromptScreen(ModalScreen[bool]):
    """Screen with a dialog to quit."""

    DEFAULT_CSS = """
        PromptScreen {
            align: center middle;
            Grid {
                height: 11;
                width: 60;
                grid-size: 2;
                border: thick $surface;
            }

            Static {
                column-span: 2;
                text-align: center;
                height: 3;
                padding: 1;
                text-style: bold;
                color: $text;
            }

            Button {
                width: 100%;
                margin: 1;
            }
        }
    """

    def __init__(self, prompt: str) -> None:
        self.prompt = prompt
        super().__init__()

    def compose(self) -> ComposeResult:
        with Grid():
            yield Static(f"Do You Want to {self.prompt}?")
            yield Button("Yes", id="yes")
            yield Button("No", variant="error", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)