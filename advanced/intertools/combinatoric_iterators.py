from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
'''
product
permutations
combinations
combinations_with_replacement
'''

# product -> This tool computes the cartesian product of input iterables.
#         -> The output of this function is tuples in sorted order.
print("======product======")

data1 = [1, 2, 3, 4, 5]
data2 = ['A', 'B', 'C', 'D', 'E']
data3 = ['A', 'B', 'C', 'D', 'E']

print(tuple(product(data1, data2))) # Accepts multiple iterators.

# permutations -> It is used to generate all possible permutations of an iterable.
#              -> All elements are treated as unique based on their position and not their values.

print("======Permutations======")
print(list(permutations('AB')))

# combinations -> Prints all the possible combinations(without replacement)

print("======Combinations======")
print(list(combinations(['A', 2, 3], 2)))

# Combinations with replacement ->

print("======Combinations with replacement======")
print(list(combinations_with_replacement(['A', 2, 3], 2)))
