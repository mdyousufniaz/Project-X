from textual.app import App
from Widgets.expression import Expression

class MyApp(App):

    def compose(self):
        yield Expression('Test', set((0, 11, 3)), set(()))

MyApp().run()