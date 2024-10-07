from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Button, Placeholder, Header, Footer, Static, Select
from textual.containers import ScrollableContainer, Center, Horizontal, Vertical
from textual import on
from textual.binding import Binding
from textual.css.query import DOMQuery, NoMatches

from widgets import FunctionCard, BEGWelcome

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
                with ScrollableContainer(id="term-body"):
                    yield BEGWelcome()

            with TabPane("Boolean Expression", id="boolean-exp"):
                yield Placeholder("Bool")
        yield Footer()

    def term_body(self) -> DOMQuery[ScrollableContainer]:
        return self.query_exactly_one("#term-body", ScrollableContainer)
    
    def welcome(self) -> DOMQuery[BEGWelcome] | None:
        try:
            return self.term_body().query_exactly_one(BEGWelcome)
        except NoMatches:
            return None


    def action_add_function_card(self) -> None:
        welcome_widget = self.welcome()
        if welcome_widget:
            welcome_widget.remove()

        new_func_card = FunctionCard()
        self.term_body().mount(new_func_card)
        new_func_card.scroll_visible()

    async def on_function_card_delete(self, event: FunctionCard.Delete) -> None:
        await event.func_card.remove()
        
        if self.func_cards():
            self.func_cards().last().scroll_visible()
        else:
            self.term_body().mount(BEGWelcome())

    def func_cards(self) -> DOMQuery[FunctionCard]:
        return self.query(FunctionCard)
    
    def action_reset_terms_tab(self) -> None:

        func_cards = self.func_cards()
        if func_cards:
            func_cards.remove()
            self.term_body().mount(BEGWelcome())
        

    def action_generate_functions(self) -> None:
        valid: bool = True

        for func_card in self.func_cards():
            if not func_card.is_valid():
                valid = False
                break
        
        if valid: self.notify(str(valid))

    
    def on_begwelcome_get_started(self) -> None:
        self.query_exactly_one(BEGWelcome).remove()
        self.action_add_function_card()

    

if __name__ == "__main__":
    BooleanExpressionGenerator().run()