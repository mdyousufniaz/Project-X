from textual.widgets import Input
from textual.events import Key

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