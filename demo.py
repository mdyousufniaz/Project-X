from textual.app import App
from widgets import CustomInput

class MyApp(App):

    CSS = """
    Screen {
        CustomInput {
            margin-top: 1;
        }
    }

    """

    def compose(self):
        yield CustomInput("Input 1", "demo", True)

MyApp().run()