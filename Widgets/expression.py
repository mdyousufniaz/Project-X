from textual.containers import Horizontal
from textual.widgets import Static

from sympy import symbols
from sympy.logic import SOPform

from math import ceil, log2


class Expression(Horizontal):

    DEFAULT_CSS = """
        Expression {
            background: $primary-background;
            padding-left: 2;
            height: auto;
            border: $success;
            #fn_name {
                width: auto;
                text-style: italic;
            }
        }
        
    """


    def __init__(self, fn_name: str, min_terms: set[int], dont_care_terms: set[int]) -> None:
        self.fn_name = fn_name
        self.min_terms = min_terms
        self.dont_care_terms = dont_care_terms
        super().__init__(
            Static(f"{fn_name} = ", id="fn_name"),
            Static(f"{self.genarate_expression()}", id='exp')
        )

    def genarate_expression(self) -> str:
        if indexes := self.min_terms | self.dont_care_terms:
            max_index = max(indexes)
            if max_index == 0:
                max_index = 1
        else: 
            max_index = 1

        return SOPform(
            symbols(f'x0:{ceil(log2(max_index + 1))}')[::-1],
            self.min_terms,
            self.dont_care_terms
        ).__str__()