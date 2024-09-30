from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class MyButton(Button):
    pass


class MyApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Normal Button")

    @on(MyButton.Pressed)
    def notify_on_press_my_button(self) -> None:
        self.notify("MyButton.Pressed matched!")


if __name__ == "__main__":
    MyApp().run()