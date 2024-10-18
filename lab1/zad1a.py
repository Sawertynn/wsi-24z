import itertools as it
from time import perf_counter
import numpy as np
from matplotlib import pyplot as plt

from knapsack import KnapSack

# first testing scenario
profits = np.array([16, 8, 9, 6])
weights = np.array([8, 3, 5, 2])
capacity = 9
correct_ans = [1, 2]

sack = KnapSack(profits, weights, capacity)
ans = sack.solve_knapsack_brute_force()
sack.print_answer(ans)

ans2 = sack.solve_knapsack_pw_ratio()
print(ans2, sack.s_profit(ans2), sack.s_weight(ans2))
sack.print_answer(ans2)

def analyze_solver(profits, weights, capacity):
    maxSize = len(profits)
    results = []
    for size in range(1, maxSize+1):
        sack = KnapSack(profits[:size], weights[:size], capacity)
        start = perf_counter()
        sack.solve_knapsack_brute_force()
        stop = perf_counter()
        duration = stop - start
        results.append((size, stop - start))
        print(f'{size:2} {duration:.2e}')
    return results


profits = np.array([16, 8, 9, 6, 7,   3, 6, 10, 12, 4])
weights = np.array([8, 3, 5, 2, 3,    1, 4, 4, 6, 5])
capacity = 9

results = analyze_solver(profits, weights, capacity)
print(results)


def measure_brute_force(maxSize: int, capacity=9):
    results = []
    profits = []
