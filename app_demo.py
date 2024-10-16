from textual.app import App
from Widgets.function_name_input import FunctionNameInput
from Widgets.beg_welcome import BEGWelcome
from Widgets.term_input import TermInput
from Widgets.function_card import FunctionCard
from textual import on
from textual.widgets import Button

class MyApp(App):

    def compose(self):
        yield FunctionCard()
    
    def on_input_submitted(self):
        value = self.query_one(FunctionCard).is_valid()
        self.notify(str(value))
    

MyApp().run()