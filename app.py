from textual.app import App
from textual.widgets import TabbedContent, TabPane, Input, Placeholder, Header, Footer, Static, Select
from textual.containers import Vertical, Center

from widgets import Function

class BooleanExpressionGenerator(App):

    TITLE = "Boolean Expression Generator"
    SUB_TITLE = "An App to generate boolean Functions!"

    CSS = """
        Select {
            align: center middle;
            width: 50%;
        }
    """

    def compose(self):
        yield Header()
        with TabbedContent(initial="terms"):
            with TabPane("Trems", id="terms"):
                with Vertical():
                    with Center():
                        yield Select.from_values(range(1, 11), prompt="Select the number of Literals")
                    yield Function()
            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
            with TabPane("Truth Table", id="truth-table"):
                yield Placeholder("Truth Table")
        yield Footer()

if __name__ == "__main__":
    BooleanExpressionGenerator().run()