from dataclasses import dataclass
from textual.message import Message

@dataclass
class Notification(Message):
    message: str
    title: str
    severity: str = "information"