from textual.containers import Center, Vertical, Horizontal, Container
from textual.widgets import Static, Input, Button
from textual.widget import Widget
from textual import on

class CustomInput(Widget):

    DEFAULT_CSS = """
        CustomInput {
            content-align: center middle;
            margin: 1;
            height: auto;
            
            Static {
                # background: blue;
                content-align: center middle;
                width: auto;
            }

            Input {
                width: 80%;
            }
        }
    """

    def __init__(self, label, placeholder, required = True):
        label += ' '
        if required:
            label += '*'

        self.label = label
        self.input = Input(placeholder=placeholder)
        super().__init__()

    def compose(self):
        with Center():
            yield Static(self.label)
            yield self.input

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

    def __init__(self):
        self.func_name = CustomInput("Function Name", "Enter the name of the function eg: X, Y, Z")
        self.min_terms = CustomInput("Minterms", "1-3, 4-6, 7, 10...")
        self.dont_care_terms = CustomInput("Don't Care Terms", "11-13, 14-16, 17, 20...", False)
        super().__init__()
    
    def compose(self):
            with Horizontal():
                yield Static("Function Card")
                yield Button("Delete", variant="error", id="delete")
            yield self.func_name
            yield self.min_terms
            yield self.dont_care_terms
            yield Static("* required", id="footnote")

    @on(Button.Pressed, "#delete")
    def delete_function_card(self):
        self.remove()
