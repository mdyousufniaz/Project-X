from textual.widgets import Static
from textual.containers import Vertical
from textual.app import ComposeResult

class NothingToShow(Vertical):

    DEFAULT_CSS = """
        NothingToShow {
            align: center middle;
            color: $text-muted;
            background: $secondary-background;
            height: 1fr;

            Static {
                text-align: center;
            }
        }
    """

    def __init__(self, action_name : str) -> None:
        super().__init__(
            Static("Noting to show!"),
            Static(f"[b]To generate [i]expressions[/i] go to [@click=app.{action_name}]Terms[/][/b]")
        )