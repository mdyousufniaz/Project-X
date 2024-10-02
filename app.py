from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Button, Placeholder, Header, Footer, Static, Select
from textual.containers import VerticalScroll, Center, Horizontal, Vertical
from textual import on

from widgets import FunctionCard

class BooleanExpressionGenerator(App):
    """
    A Textual App that takes Functions truth value as input and gives boolean expression as output.
    It can also show the coressponding truth table acrroding to input and output.
    """

    TITLE = "Boolean Expression Generator"
    SUB_TITLE = "An App to generate boolean Functions!"

    CSS = """
    Screen {
        TabbedContent {
            TabPane {
                Placeholder {
                    height: 1fr;
                    width: 1fr;
                }
            }
        }
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Terms", id="terms"):
                yield Placeholder("Terms")
            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
        yield Footer()

    

if __name__ == "__main__":
    BooleanExpressionGenerator().run()