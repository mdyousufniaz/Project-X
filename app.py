from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Button, Placeholder, Header, Footer, Static, Select
from textual.containers import VerticalScroll, Center, Horizontal, Vertical
from textual import on
from textual.binding import Binding
from textual.css.query import DOMQuery

from widgets import FunctionCard

class BooleanExpressionGenerator(App):
    """
    A Textual App that takes Functions truth value as input and gives boolean expression as output.
    It can also show the coressponding truth table acrroding to input and output.
    """

    BINDINGS = [
        Binding('ctrl+a', "add_function_card", "Add Function Card", priority=True, tooltip="Add a new Function Card"),
        Binding('ctrl+r', "reset_terms_tab", "Reset", tooltip="Reset to Default"),
        Binding('ctrl+g', "generate_functions", "Generate", tooltip="Generate boolean Functions")
    ]

    TITLE = "Boolean Expression Generator"
    SUB_TITLE = "An App to generate boolean Functions!"

    CSS = """
    Screen {
        TabbedContent {
            #terms {
                
            }
        }
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Terms", id="terms"):
                with VerticalScroll():
                    yield Select.from_values(
                        range(2, 11),
                        prompt="Select Number of literals"
                    )

            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
        yield Footer()

    def action_add_function_card(self) -> None:
        self.query_exactly_one(VerticalScroll).mount(FunctionCard())

    def on_function_card_delete(self, event: FunctionCard.Delete) -> None:
        event.func_card.remove()

    def func_cards(self) -> DOMQuery[FunctionCard]:
        return self.query(FunctionCard)
    
    def action_reset_terms_tab(self) -> None:
        select: Select = self.query_exactly_one(Select)

        if not select.is_blank():
            select.clear()
        if select.expanded:
            select.expanded = False

        func_cards = self.func_cards()
        if func_cards:
            func_cards.remove()

    def action_generate_functions(self) -> None:
        valid: bool = True

        for func_card in self.func_cards():
            if not func_card.is_valid():
                valid = False
                break


    

if __name__ == "__main__":
    BooleanExpressionGenerator().run()