from .labeled_input import LabeledInput
from textual.validation import Function
from textual.events import Key


class FunctionNameInput(LabeledInput):
    """A Custom Name Input class to receive the function name"""


    def __init__(self) -> None:
        super().__init__("Function Name *", "Name of the function like X, Y, Z")
    
    def on_mount(self) -> None:
        self.max_length = 10
        self.validators.append(Function(lambda value: value != ''))

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

    def is_valid(self) -> bool:
        if self.value:
            return True
               
        self.notify(
                "The Value of the Input can't be Empty!",
                title="Empty Error",
                severity="error"
            )
        self.focus()
        return False