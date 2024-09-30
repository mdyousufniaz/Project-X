from textual.app import App
from textual.widgets import TabbedContent, TabPane, Button, Placeholder, Header, Footer, Static, Select
from textual.containers import VerticalScroll, Center, Horizontal, Vertical
from textual import on

from widgets import FunctionCard

class BooleanExpressionGenerator(App):

    TITLE = "Boolean Expression Generator"
    SUB_TITLE = "An App to generate boolean Functions!"

    CSS = """
        #terms {
            #term-header {
                align-horizontal: center;
                margin-bottom: 1;
                height: auto;
                Select {
                    width: 50%;
                }
            }
        }
    """

    def compose(self):
        yield Header()
        with TabbedContent(initial="terms"):
            with TabPane("Trems", id="terms"):
                with VerticalScroll():
                    with Horizontal(id="term-header"):
                        yield Select.from_values(range(1, 11), prompt="Select the number of Literals")
                        yield Button("Add Function Card", variant="success", id="add")
                    yield Center()
                        
            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
            with TabPane("Truth Table", id="truth-table"):
                yield Placeholder("Truth Table")
        yield Footer()

    @on(Button.Pressed, "#add")
    def add_function_card(self):
        self.query_one(Center).mount(FunctionCard())

if __name__ == "__main__":
    BooleanExpressionGenerator().run()