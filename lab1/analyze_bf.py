from time import perf_counter
from random import randint

import numpy as np
from matplotlib import pyplot as plt

from knapsack import KnapSack


def measure_brute_force(maxSize: int, capacity=9):
    results = []
    profits = []
    weights = []

    sizes = np.array(list(range(1, maxSize+1)))

    for size in sizes:
        w = randint(1, capacity)
        p = randint(1, 3 * w)
        profits.append(p)
        weights.append(w)
        sack = KnapSack(np.array(profits), np.array(weights), capacity)

        start = perf_counter()
        sack.solve_knapsack_brute_force()
        duration = perf_counter() - start
        results.append(duration)

    return sizes, results


sizes, results = measure_brute_force(16)

fig, ax = plt.subplots()
ax.plot(sizes, results)

ax.set(xlabel='item count', ylabel='time [s]',
       title='Knapsack Brute Force solving time')
ax.grid()

plt.show()
