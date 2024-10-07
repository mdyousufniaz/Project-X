from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Center, Vertical, Horizontal, Container
from textual.widgets import Static, Input, Button, Label, Markdown
from textual.widget import Widget
from textual.message import Message
from textual import on
from textual.events import Key
from textual.validation import Function
from textual.css.query import DOMQuery

from validator_functions import is_valid_term, convert_number

class BEGWelcome(Static):

    WELCOME_MD = """
# Welcome to **Boolean Expression Generator** App!

### *Features*:
- Add as many functions as you want.
- Validate before generating functions.
- Generate Truth Tables instantly.

### *Key Shortcuts*:
- `ctrl+a`: Add new Function Card
- `ctrl+r`: Reset to default
- `ctrl+g`: Generate Functions and Truth Table
"""

    DEFAULT_CSS = """
        BEGWelcome {
            margin: 1;
            padding-top: 1;
            padding-bottom: -1;
            border: panel $primary;
            
            Markdown {
                background: $boost;
                padding: -1 2 0 2;
            }

            Button {
                width: 100%;
                margin: 1;
            }
        }
    """

    class GetStarted(Message):

        def __init__(self) -> None:
            super().__init__()

    def compose(self) -> ComposeResult:
        yield Markdown(self.WELCOME_MD)
        yield Button("Get Statrted", "primary")

    def on_button_pressed(self) -> None:
        self.post_message(self.GetStarted())

    

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
    
    def input(self) -> DOMQuery[NotifyMaxLengthInput]:
        return self.query_exactly_one(NotifyMaxLengthInput)

    
    def is_empty(self) -> bool:

        if self.input().value:
            return False

        self.input().focus()
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
        self.input().max_length = 5
        self.input().validators.append(Function(lambda value: value.isidentifier()))

    def is_valid(self) -> bool:
        return not self.is_empty()


class TermInput(LabeledInput):

    def on_mount(self) -> None:
        self.input().validators.append(Function(is_valid_term))

    def check_value(self) -> bool:
        value = self.input().value

        if value:
            for term in value.split(','):
                if term.count('-') == 1:
                    num1, num2 = term.split('-')
                    num1 = convert_number(num1)
                    num2 = convert_number(num2)

                    if None in (num1, num2):
                        self.notify(
                            f"({term}) doesn't contain valid integer(s)!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                        return False

                    if num1 > num2:
                        self.notify(
                            f"({term}) contains a invalid range!",
                            title="Invalid Range Error",
                            severity="error"
                        )
                        return False
                elif term.count('-') > 1:
                    self.notify(
                            f"({term}) doesn't contain valid integer(s)!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                    return False      
  
                else:
                    num = convert_number(term)
                    if num == None:
                        self.notify(
                            f"({term}) isn't a valid integer!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                        return False
                
                
                    
        return True

    def is_valid(self) -> bool:
        if self.check_value():
            if self.required and self.is_empty():
                self.input().focus()
                return False
            return True
        
        self.input().focus()
        return False



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
        if self.query_exactly_one(FunctionNameInput).is_valid():

            for term_input in self.query(TermInput):
                if not term_input.is_valid():
                    return False
            return True
        
        return False
    
    def truth_values(self) -> set[int]:
        ...