from textual.app import App
from widgets import LabeledInput

class MyApp(App):

    CSS = """

    """

    def compose(self):
        yield LabeledInput('Hello')

MyApp().run()

