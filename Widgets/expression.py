from textual.containers import Horizontal
from textual.widgets import Markdown

from sympy import symbols
from sympy.logic import SOPform

from math import ceil, log2


class Expression(Horizontal):

    def __init__(self, fn_name: str, min_terms: set[int], dont_care_terms: set[int]) -> None:
        self.fn_name = fn_name
        self.min_terms = min_terms
        self.dont_care_terms = dont_care_terms
        super().__init__(
            Markdown(f"**{fn_name}** = "),
            Markdown(f"*{self.genarate_expression()}*")
        )

    def genarate_expression(self) -> str:
        if indexes := self.min_terms + self.dont_care_terms:
            max_index = max(indexes)
            if max_index == 0:
                max_index = 1
        else: 
            max_index = 1

        return str(SOPform(
            symbols(f'A0:{ceil(log2(max_index + 1))}')[::-1],
            self.min_terms,
            self.dont_care_terms
        ))