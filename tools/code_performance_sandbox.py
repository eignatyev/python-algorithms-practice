from random import randint
from timeit import timeit

from src.lists import FindPairAlgorithms

r = 1000
v = randint(-r * 2 + 1, r * 2 -1)
inp = [randint(-r, r) for _ in range(r * 2 + 1)]
sorted_inp = sorted(inp)

r1 = timeit(lambda: FindPairAlgorithms.iteration(inp, v), number=10)
r2 = timeit(lambda: FindPairAlgorithms.two_pointer(sorted_inp, v), number=10)

print(f'Target value: {v}\n\nInput list: {inp}\n\nSorted input: {sorted_inp}\n')
print(FindPairAlgorithms.iteration(inp, v))
print(FindPairAlgorithms.two_pointer(sorted_inp, v))
print( f'{r1 - r2:.9f}')
