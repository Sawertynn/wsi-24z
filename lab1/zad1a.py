import numpy as np
import itertools as it

from knapsack import KnapSack

# first testing scenario
profits = np.array([16, 8, 9, 6])
weights = np.array([8, 3, 5, 2])
capacity = 9
correct_ans = [1, 2]

sack = KnapSack(profits, weights, capacity)
ans = sack.solve_knapsack_brute_force()
print(ans)
# assert np.array_equal(ans, correct_ans)


sack.solve_knapsack_pw_ratio()