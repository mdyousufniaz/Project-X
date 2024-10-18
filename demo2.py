from sympy import symbols
from sympy.logic import POSform

from math import ceil, log2

minterm_indexes = [0, 1, 2]
dont_care_indexes = []

variables = symbols(
        f'x0:{ceil(log2(max(minterm_indexes + dont_care_indexes) + 1))}'
    )[::-1]

print(variables)

print(POSform(
    variables,
    minterm_indexes,
    dont_care_indexes
))

print(symbols('x0:0'))