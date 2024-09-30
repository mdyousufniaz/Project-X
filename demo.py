from textual.app import App, ComposeResult
from textual.widgets import Placeholder, TabbedContent, TabPane


class MinimalApp(App[None]):
    CSS = """
        Placeholder {
            width: 1fr;
            height: 1fr;
        }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("First tab"):
                yield Placeholder("This is a minimal app.")
            with TabPane("Second tab"):
                yield Placeholder("Another tab.")


MinimalApp().run()