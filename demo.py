from textual.app import App
from widgets import FunctionCard

class MyApp(App):

    CSS = """

    """

    def compose(self):
        yield FunctionCard()

MyApp().run()

