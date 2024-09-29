from textual.app import App
from textual.widget import Widget
from textual.widgets import Static
from textual.events import MouseDown, MouseUp, Click

class CustomButton(Widget):
    DEFAULT_CSS = """
        CustomButton {
            background: $accent;
            height: auto;
            width: auto;
            padding: 0 2;
            outline-left: thick blue;
            outline-right: thick blue;
            Static {
                height: auto;
                width: auto;
            }
        }
    """

    def compose(self):
        yield Static("Test")

    # Handle MouseDown event
    def on_mouse_down(self, event: MouseDown) -> None:
        self.app.log("Mouse Down on CustomButton!")

    # Handle MouseUp event
    def on_mouse_up(self, event: MouseUp) -> None:
        self.app.log("Mouse Up on CustomButton!")

    # Handle Click event
    def on_click(self, event: Click) -> None:
        self.app.log("CustomButton Clicked!")


class MyApp(App):
    def compose(self):
        yield CustomButton()


MyApp().run()
