from textual.app import App
from widgets import BEGWelcome
from textual.widgets import Welcome

class MyApp(App):

    CSS = """

    """

    def compose(self):
        yield BEGWelcome()
        # yield Welcome()

MyApp().run()

