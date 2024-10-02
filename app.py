from textual.app import App
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
        #terms {
            #term-header {
                align-horizontal: center;
                margin-bottom: 1;
                height: auto;
                Select {
                    width: 50%;
                }
            }

            #default {
                background: $boost;
                text-align: center;
                height: 90h;
                content-align: center middle;
                color: $text-muted;
            }
        }
    """
    default_message = Static("There is Nothing to Display !", id="default")



    def compose(self):
        yield Header()
        with TabbedContent(initial="terms"):
            with TabPane("Trems", id="terms"):
                with VerticalScroll():
                    with Horizontal(id="term-header"):
                        yield Select.from_values(range(2, 11), prompt="Select the number of Literals")
                        yield Button("Add Function Card", variant="success", id="add")
                    with Center(id="func-body"):
                        yield self.default_message 
                        
            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
        yield Footer()

    def func_cards(self):
        return self.query_one(Center).query(FunctionCard)

    @on(Button.Pressed, "#add")
    def add_function_card(self):
        if not self.func_cards():
            self.query_one(Center).remove_children()
        self.query_one(Center).mount(FunctionCard())
    
    async def on_function_card_delete(self, message):
        await message.func_card.remove()
        if not self.func_cards():
            self.query_one(Center).mount(self.default_message)

if __name__ == "__main__":
    BooleanExpressionGenerator().run()