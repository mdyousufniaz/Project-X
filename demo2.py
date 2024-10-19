from sympy import symbols
from sympy.logic import POSform

from math import ceil, log2

minterm_indexes = [0]
dont_care_indexes = []

indexes = minterm_indexes + dont_care_indexes

if indexes:
    max_index = max(minterm_indexes + dont_care_indexes)

    if max_index == 0:
        max_index = 1
else:
    max_index = 1


variables = symbols(
        f'x0:{ceil(log2(max_index + 1))}'
    )[::-1]

print(variables)

print(type(POSform(
    variables,
    minterm_indexes,
    dont_care_indexes
)))
