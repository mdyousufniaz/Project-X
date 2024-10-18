from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Button, Label, Header, Footer, Static, Select
from textual.containers import ScrollableContainer, Center, Horizontal, Vertical
from textual import on, work
from textual.binding import Binding
from textual.css.query import DOMQuery, NoMatches

from Widgets.beg_welcome import BEGWelcome
from Widgets.function_card import FunctionCard
from Widgets.label_with_button import LabelWithButton
from Widgets.nothing_to_show import NothingToShow

from Screens.prompt_screen import PromptScreen

class BooleanExpressionGenerator(App):
    """
    A Textual App that takes Functions truth value as input and gives boolean expression as output.
    It can also show the coressponding truth table acrroding to input and output.
    """

    BINDINGS = [
        Binding('ctrl+n', "add_function_card", "Add Function Card", tooltip="Add a new Function Card"),
        Binding('ctrl+r', "reset_terms_tab", "Reset", tooltip="Reset to Default"),
        Binding('ctrl+g', "generate_functions", "Generate", tooltip="Generate boolean Functions"),
        Binding('ctrl+q', "quit", "Quit", tooltip="Quit the application")
    ]


    TITLE = "Boolean Expression Generator"
    SUB_TITLE = "An App to generate boolean Functions!"
    CSS_PATH = "app.tcss"

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
                with Horizontal(classes='banner'):
                    yield Label("Expressions")
                    yield Button(
                        "Truth Table",
                        "primary",
                        disabled=True,
                        id="truth-table",
                        tooltip="Press to generate Truth Table"
                    )
                with ScrollableContainer(id="exp-body"):
                    yield NothingToShow("go_to_terms")
        yield Footer()



    def term_body(self) -> DOMQuery[ScrollableContainer] | None:
        return self.query_exactly_one("#term-body", ScrollableContainer)
    
    def welcome(self) -> DOMQuery[BEGWelcome] | None:
        try:
            return self.term_body().query_exactly_one(BEGWelcome)
        except NoMatches:
            pass


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
    
    @work
    async def action_reset_terms_tab(self) -> None:
        if await self.push_screen_wait(PromptScreen('reset')):
            func_cards = self.func_cards()
            if func_cards:
                func_cards.remove()
                self.term_body().mount(BEGWelcome())

    @work    
    async def action_quit(self) -> None:
        if await self.push_screen_wait(PromptScreen('quit')):
            self.exit()
        

    def action_generate_functions(self) -> None:
        valid: bool = True

        for func_card in self.func_cards():
            if not func_card.is_valid():
                valid = False
                break
        
        if valid:
            for func_card in self.func_cards():
                print(func_card.truth_indices())

    @on(Button.Pressed, '#get-started')
    def get_started(self) -> None:
        self.query_exactly_one(BEGWelcome).remove()
        self.action_add_function_card()

    def on_tabbed_content_tab_activated(self):
        self.refresh_bindings()

    def check_action(self, action: str, parameters:tuple[object, ...]) -> bool | None:
        if action in ("add_function_card", "reset_terms_tab", "generate_functions"):
            try:
                if self.query_exactly_one(TabbedContent).active != 'terms':
                    return None
            except NoMatches:
                pass
        return True

    def action_go_to_terms(self) -> None:
        self.query_exactly_one(TabbedContent).active = 'terms'
    

if __name__ == "__main__":
    BooleanExpressionGenerator().run()