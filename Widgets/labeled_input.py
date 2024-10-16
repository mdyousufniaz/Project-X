from .notify_max_length_input import NotifyMaxLengthInput
from textual.containers import Container
from textual.css.query import DOMQuery
from textual.validation import Function
from textual.widgets import Input

class LabeledInput(Input):

    """
    A Custom widget Class of reciveing input from user with a Label.
    """

    DEFAULT_CSS = """
        LabeledInput {
            border-title-style: italic;
            border-title-color: white;
        }
    """


    def __init__(self, label: str, placeholder: str) -> None:
        super().__init__(placeholder=placeholder)
        self.border_title = label


    
    