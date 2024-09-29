from textual.containers import Center, Vertical, Horizontal, Middle
from textual.widgets import Static, Input
from textual.widget import Widget

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
                width: 50%
            }
        }
    """

    def __init__(self, label, placeholder, optional = True):
        label += ' '
        if not optional:
            label += '*'

        self.label = label
        self.input = Input(placeholder=placeholder)
        super().__init__()

    def compose(self):
        with Center():
            yield Static(self.label)
            yield self.input

class Function(Vertical):

    DEFAULT_CSS = """
        Function {
            #test {
                background: green;
                Static {
                    background: red;
                    width: auto;
                }
            }
        }
    """

    def __init__(self):
        self.func_name = CustomInput("Function Name", "Enter the name of the function eg: X, Y, Z")
        self.min_terms = CustomInput("Minterms", "1-3, 4-6, 7, 10...", False)
        self.dont_care_terms = CustomInput("Don't Care Terms", "11-13, 14-16, 17, 20...")
        super().__init__()
    
    def compose(self):
        with Center():
            with Center(id="test"):
                yield Static("Function Card")
                yield Static("Delete")
            yield self.func_name
            yield self.min_terms
            yield self.dont_care_terms

