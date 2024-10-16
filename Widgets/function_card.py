from __future__ import annotations

from textual.containers import Center, Vertical, Horizontal
from textual.app import ComposeResult
from textual.widgets import Label, Button, Static
from textual.message import Message

from .function_name_input import FunctionNameInput
from .term_input import TermInput

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

                LabeledInput {
                    margin: 1 0;
                }

                #footnote {
                    text-align: right;
                    text-style: italic;
                    padding-right: 1;
                    background: $primary-background;
                }
            }

            Vertical:focus-within {
                border: round $success;
            }
        }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Label("Function Card")
                yield Button("Delete", variant="error")
            yield FunctionNameInput()
            yield TermInput("Min Terms", "terms like 1 - 3, 4 - 7, 8, 10")
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
    
    def truth_indices(self) -> set[int]:
        ones_indexes: set[int] = set()

        for term in self.query(TermInput):
            for literal in term.input().value.split(','):
                if literal.find('-') != -1:
                    num1, num2 = literal.split('-')
                    ones_indexes.update(range(
                        int(num1),
                        int(num2) + 1
                    ))

                else:
                    ones_indexes.add(int(literal))
            
            return ones_indexes