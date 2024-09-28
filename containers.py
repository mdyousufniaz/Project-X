from textual.containers import VerticalScroll, Vertical
from textual.widgets import Static, Input

class TitledVerticalScroll(VerticalScroll):
    DEFAULT_CSS = """
        TitledVerticalScroll {
            border: round $warning;
            border-title-style: italic;
        }
    """

    def __init__(self, title):
        self.BORDER_TITLE = title
        super().__init__()

class Section(Vertical):

    DEFAULT_CSS = """
        Section {
            #header {
                background: $panel;
                height: auto;
                Static {
                    padding-bottom: 1;
                }

                #title {
                    text-style: bold;
                }

                #sub-title {
                    color: $text-muted;
                    text-style: italic;
                    padding-left: 4;
                }
            }
        }
    """

    def compose(self):
        with Vertical(id="header"):
            yield Static(self.title, id="title")
            yield Static(self.sub_title, id="sub-title")
        yield self.body
        

    def __init__(self, title, sub_title):
        self.title = title
        self.sub_title = sub_title
        self.body = Vertical()
        super().__init__()

class BooleanSection(Section):

    DEFAULT_CSS = """
        
    """

    def __init__(self):
        super().__init__("Boolean Expression", "Enter the correct boolean expression") 

class CustomInput(Input):

    def __init__(self, message):
        self.message = message
