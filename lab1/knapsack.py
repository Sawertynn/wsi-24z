import numpy as np
import itertools as it


class KnapSack:
    def __init__(self, profits, weights, capacity):
        if len(profits) != len(weights):
            raise ValueError("profits and weights arrays must be equal in length")
        self.profits = profits
        self.weights = weights
        self.capacity = capacity

    def solve_knapsack_brute_force(self) -> np.ndarray[int]:
        best_profit = 0
        best_indexes = None
        indexes = np.array(range(len(self.profits)))
        maxSize = len(self.profits) + 1

        for size in range(1, maxSize):
            for subset in it.combinations(indexes, size):
                chosen = np.array(subset).astype(int)
                if self._fits(chosen) and self.profits[chosen].sum() > best_profit:
                    best_indexes = chosen
                    best_profit = self.profits[chosen].sum()
        return best_indexes

    def solve_knapsack_pw_ratio(self) -> np.ndarray[int]:
        indexes = list(range(len(self.profits)))
        indexes.sort(key=lambda ind: self.profits[ind] / self.weights[ind], reverse=True)

        best_indexes = []
        current_weight = 0
        for i, w in zip(indexes, self.weights[indexes]):
            if w + current_weight <= self.capacity:
                best_indexes.append(i)
                current_weight += w
            if current_weight == self.capacity:
                break
        return best_indexes

    # Utility methods
    def s_profit(self, indexes):
        return sum(self.profits[indexes])

    def s_weight(self, indexes):
        return sum(self.weights[indexes])
    
    def print_answer(self, indexes):
        s = f'answer: {indexes}, total profit: {self.s_profit(indexes)}, weight: {self.s_weight(indexes)}/{self.capacity}'
        print(s)

    def _fits(self, indexes) -> bool:
        return sum(self.weights[indexes]) < self.capacity
