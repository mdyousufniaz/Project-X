from textual.app import ComposeResult
from textual.widgets import Static, Markdown, Button
from textual.message import Message

class BEGWelcome(Static):

    WELCOME_MD = """
# Welcome to **Boolean Expression Generator** App!

### *Features*:
- Add as many functions as you want.
- Validate before generating functions.
- Generate Truth Tables instantly.

### *Key Shortcuts*:
- `ctrl+a`: Add new Function Card
- `ctrl+r`: Reset to default
- `ctrl+g`: Generate Functions and Truth Table
"""

    DEFAULT_CSS = """
        BEGWelcome {
            margin: 1;
            padding-top: 1;
            padding-bottom: -1;
            border: panel $primary;
            
            Markdown {
                background: $boost;
                padding: -1 2 0 2;
            }

            Button {
                width: 100%;
                margin: 1;
            }
        }
    """

    def compose(self) -> ComposeResult:
        yield Markdown(self.WELCOME_MD)
        yield Button("Get Statrted", "primary", id="get-started")