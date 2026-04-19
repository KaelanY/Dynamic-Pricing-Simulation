import random
import math
from .base import BaseStrategy

class AdaptiveExplatoryStrategyV2(BaseStrategy):
    def __init__(self):
        self.bins = [i for i in range(1, 101)]
        self.q_values = {b: 0.0 for b in self.bins}
        self.counts = {b: 0 for b in self.bins}

        self.last_price = 10
        self.temperature = 2.0

        self.best_price = 10
        self.best_value = float("-inf")

        self.alpha = 0.1

    def _closest_bin(self, price):
        return min(self.bins, key=lambda x: abs(x - price))

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        b = self._closest_bin(self.last_price)
        self.counts[b] += 1

        self.q_values[b] += self.alpha * (last_profit - self.q_values[b])

        if last_profit > self.best_value:
            self.best_value = last_profit
            self.best_price = self.last_price

        self.temperature = max(0.1, self.temperature * 0.995)

        if random.random() < 0.1:
            price = random.uniform(1, 100)
        else:
            max_q = max(self.q_values.values())
            weights = [
                math.exp((self.q_values[b] - max_q) / self.temperature)
                for b in self.bins
            ]

            total = sum(weights)
            probs = [w / total for w in weights]

            chosen_bin = random.choices(self.bins, weights=probs, k=1)[0]

            price = chosen_bin + random.uniform(-2, 2)

        if random.random() < 0.2:
            price = self.best_price + random.uniform(-1, 1)

        self.last_price = max(0.1, min(100, price))
        return self.last_price
