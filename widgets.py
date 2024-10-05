from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Center, Vertical, Horizontal, Container
from textual.widgets import Static, Input, Button, Label, Pretty
from textual.widget import Widget
from textual.message import Message
from textual import on
from textual.events import Key
from textual.validation import Function

from validator_functions import is_valid_term


class NotifyMaxLengthInput(Input):
    
    def on_key(self, event: Key) -> None:
        if (self.max_length
             and len(self.value) == self.max_length
             and event.is_printable
        ):
            self.notify(
                f"Input can not exceed {self.max_length} characters!",
                title="Max Length Warning",
                severity="warning"
            )

class LabeledInput(Container):

    """
    A Custom widget Class of reciveing input from user with a Label and a required option.
    """

    DEFAULT_CSS = """
    LabeledInput {
        background: $boost;
        margin: 1;
        border-title-style: italic;
        height: auto;
        border: blank white;
    }
    """


    def __init__(self, label: str, placeholder: str = '', required = False) -> None:
        """Initializer of the CustomInput Class

        Args:
            label (str): The label for the Custom Input.
            placeholder (str, optional): placeholder for the custom input. Defaults to ''.
            required (bool, optional): The input is requied or not. Defaults to False.
        """

        self.required: bool = required
        if self.required:
            label += " *" # adding required symbol

        super().__init__(
            NotifyMaxLengthInput(
                placeholder=placeholder,
                validators=[
                    Function(lambda value: value != '')
                ] if required else None
            )
        )

        self.border_title = label
    
    def is_empty(self) -> bool:
        input = self.query_exactly_one(NotifyMaxLengthInput)
        if input.value:
            return False

        input.focus()
        self.notify(
                "The Value of the Input can't be Empty!",
                title="Empty Error",
                severity="error"
            )
        return True

     



class FunctionNameInput(LabeledInput):
    """A Custom Name Input class to receive the function name"""


    def __init__(self) -> None:
        super().__init__("Function Name", "Name of the function like X, Y, Z", True)
    
    def on_mount(self) -> None:
        self.query_exactly_one(NotifyMaxLengthInput).max_length = 5

    def is_valid(self) -> bool:
        return not self.is_empty()


class TermInput(LabeledInput):

    def on_mount(self) -> None:
        self.query_exactly_one(NotifyMaxLengthInput).validators.append(Function(is_valid_term))


class FunctionCard(Center):
    """A class for a custom widget to receive function credentials from user."""

    DEFAULT_CSS = """
        FunctionCard {
            Vertical {
                background: $panel;
                width: 70%;
                height: auto;
                margin: 1;
                padding-top: 1;
                Horizontal {
                    height: 3;
                    padding-left: 2;
                    align-vertical: middle;

                    Label {
                        color: $secondary;
                    }

                    Button {
                        dock: right;
                    }
                }

                #footnote {
                    text-align: right;
                    text-style: italic;
                    padding-right: 1;
                    background: $primary-background;
                }
            }

            Vertical:focus-within {
                border: ascii $success;
            }
        }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Label("Function Card")
                yield Button("Delete", variant="error")
            yield FunctionNameInput()
            yield TermInput("Min Terms", "terms like 1 - 3, 4 - 7, 8, 10", True)
            yield TermInput("Don't Care Terms", "terms like 10 - 13, 14 - 16, 18")
            yield Static("* required", id="footnote")

    class Delete(Message):

        def __init__(self, func_card: FunctionCard) -> None:
            self.func_card = func_card
            super().__init__()


    def on_button_pressed(self) -> None:
        self.post_message(self.Delete(self))

    def is_valid(self) -> bool:
        return self.query_exactly_one(FunctionNameInput).is_valid()