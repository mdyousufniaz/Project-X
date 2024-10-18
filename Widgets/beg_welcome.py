from textual.app import ComposeResult
from textual.widgets import Static, Markdown, Button

class BEGWelcome(Static):

    WELCOME_MD = """
# Welcome to **Boolean Expression Generator** App!

### *Features*:
- Add as many functions as you want.
- Validate before generating functions.
- Generate Truth Tables instantly.

### *Key Shortcuts*:
- `ctrl+n`: Add new Function Card
- `ctrl+r`: Reset to default
- `ctrl+g`: Generate Functions
- `ctrl+q`: Quit the application
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
                height: 1fr;
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