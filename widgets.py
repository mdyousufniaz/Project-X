from textual.app import ComposeResult
from textual.containers import Center, Vertical, Horizontal, Middle
from textual.widgets import Static, Input, Button, Label, Pretty
from textual.widget import Widget
from textual.message import Message
from textual import on
from textual.validation import Validator, ValidationResult

class CustomInput(Center):

    """
    A Custom widget Class of reciveing input from user with a Label and a required option.
    """

    DEFAULT_CSS = """
    CustomInput {
        background: $boost;
    }
    """

    def __init__(self, label: str, placeholder: str = '', required = False) -> None:
        """Initializer of the CustomInput Class

        Args:
            label (str): The label for the Custom Input.
            placeholder (str, optional): placeholder for the custom input. Defaults to ''.
            required (bool, optional): The input is requied or not. Defaults to False.
        """

        if required:
            label += " *" # adding required symbol

        super().__init__(
            Label(label),
            Input(placeholder=placeholder, valid_empty=not required)
        )


    def on_input_submitted(self, event: Input.Submitted) -> None:
        if not event.value:
            self.app.notify("Input can not be empty!")



class FunctionCard(Vertical):

    DEFAULT_CSS = """
        FunctionCard {
            background: $boost;
            height: auto;
            width: 60%;
            margin-bottom: 1;
            Horizontal {
                background: $panel;
                height: auto;
                width: 100%;
                align-horizontal: right;
                padding: 0 2;
                Static {
                        dock: left;
                        width: auto;
                        text-style: bold;
                        color: $warning;
                        height: 100%;
                        content-align: left middle;
                    }
                
            }

            #footnote {
                color: $error;
                padding-right: 1;
                text-style: italic;
                text-align: right;
                height: auto;
            }
        }
    """

    class Delete(Message):

        def __init__(self, func_card):
            self.func_card = func_card
            super().__init__()

    def __init__(self):
        self.func_name = CustomInput("Function Name", "Enter the name of the function eg: X, Y, Z",optional=False, max_length=5)
        self.min_terms = CustomInput("Minterms", "1-3, 4-6, 7, 10...")
        self.dont_care_terms = CustomInput("Don't Care Terms", "11-13, 14-16, 17, 20...")
        super().__init__()
    
    def compose(self):
            with Horizontal():
                yield Static("Function Card")
                yield Button("Delete", variant="error", id="delete")
            yield self.func_name
            yield self.min_terms
            yield self.dont_care_terms
            yield Static("* required", id="footnote")

    def check_func_name(self):
        if not self.func_name.value():
            self.func_name.focus()
            self.app.notify("Please Enter a valid Function Name!")
    
    def check_min_terms(self):
        if not self.min_terms.value():
            return False


    def check_input_values(self):
        # checking func_name
        if not self.func_name.value():
            return False
        

    @on(Button.Pressed, "#delete")
    def send_delete_message(self):
        # self.post_message(self.Delete(self))
        self.check_func_name()
