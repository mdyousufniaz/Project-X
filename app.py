from textual.app import App
from containers import TitledVerticalScroll, BooleanSection

class MyApp(App):
    def compose(self):
        with TitledVerticalScroll('Input'):
            yield BooleanSection()

if __name__ == "__main__":
    MyApp().run()