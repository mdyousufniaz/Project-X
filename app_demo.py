from textual.app import App
from Widgets.expression import Expression

class MyApp(App):

    def compose(self):
        yield Expression('Test', set((0, 1, 11)), set((5, 7)))

MyApp().run()