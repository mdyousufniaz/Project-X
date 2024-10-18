from sympy import symbols, Or, And, simplify_logic
from math import ceil, log2

# Step 1: Define the minterms and don't care terms
minterm_indexes = []
dont_care_indexes = [0, 1]

# Step 2: Determine the number of variables required
max_index = max(minterm_indexes + dont_care_indexes)
num_variables = ceil(log2(max_index + 1))

# Step 3: Generate variable symbols
variables = symbols(f'x0:{num_variables}')  # Create variables: x0, x1, x2, ...

# Step 4: Create minterm and don't care expressions
def index_to_expr(index, variables):
    """Converts a binary index to a Boolean AND expression."""
    binary = format(index, f'0{len(variables)}b')
    print(binary)
    return And(*[var if bit == '1' else ~var for var, bit in zip(variables, binary)])

# Create the minterm expressions
minterms = [index_to_expr(index, variables) for index in minterm_indexes]

print(minterms)

# Create don't care expressions
dont_cares = [index_to_expr(index, variables) for index in dont_care_indexes]

# Step 5: Combine minterms and don't cares and simplify
combined_expression = Or(*minterms, *dont_cares)

print(combined_expression)

# Step 6: Simplify the expression using `simplify_logic` with `dontcares` parameter
simplified_function = simplify_logic(combined_expression, form='dnf', dontcare=Or(*dont_cares))

# Step 7: Print results
print(f"Number of variables needed: {num_variables}")
print(f"Simplified Boolean function: {simplified_function}")
