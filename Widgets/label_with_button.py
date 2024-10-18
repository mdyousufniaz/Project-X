from textual.containers import Horizontal
from textual.widgets import Label, Button

class LabelWithButton(Horizontal):

    def __init__(self, label: str, btn_label: str) -> None:
        super().__init__(Label(label), Button(btn_label, "error"), classes='banner')