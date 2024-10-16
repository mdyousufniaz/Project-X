from .labeled_input import LabeledInput
from textual.validation import Function
from validator_functions import is_valid_term, convert_number

class TermInput(LabeledInput):

    def on_mount(self) -> None:
        self.validators.append(Function(is_valid_term))

    def check_value(self) -> bool:
        value = self.value

        if value:
            for term in value.split(','):
                if term.count('-') == 1:
                    num1, num2 = term.split('-')
                    num1 = convert_number(num1)
                    num2 = convert_number(num2)

                    if None in (num1, num2):
                        self.notify(
                            f"({term}) doesn't contain valid integer(s)!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                        return False

                    if num1 >= num2:
                        self.notify(
                            f"({term}) contains a invalid range!",
                            title="Invalid Range Error",
                            severity="error"
                        )
                        return False
                elif term.count('-') > 1:
                    self.notify(
                            f"({term}) doesn't contain valid integer(s)!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                    return False      
  
                else:
                    num = convert_number(term)
                    if num == None:
                        self.notify(
                            f"({term}) isn't a valid integer!",
                            title="Invalid Integer Error",
                            severity="error"
                        )
                        return False      
        return True

    def is_valid(self) -> bool:
        if self.check_value():
            return True
        self.focus()
        return False