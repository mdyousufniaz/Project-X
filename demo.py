from textual.app import App
from widgets import CustomInput

class MyApp(App):

    def compose(self):
        yield CustomInput("Input 1", "demo", True)

MyApp().run()