from textual.validation import Validator, ValidationResult

class Empty(Validator):
        """A Custom Validator class for checking the input is empty or not"""

        def validate(self, value: str) -> ValidationResult:
            """A method to check the input is empty or not

            Args:
                value (str): value to be checked

            Returns:
                ValidationResult: 
            """

            if value:
                return self.success()
            else:
                return self.failure("Value can not be empty")
