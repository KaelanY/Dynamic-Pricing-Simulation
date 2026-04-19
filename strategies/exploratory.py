import random
from collections import defaultdict
from .base import BaseStrategy

class MLExploratoryStrategy(BaseStrategy):
    def __init__(self, epsilon=0.2):
        self.epsilon = epsilon
        self.q_values = defaultdict(float)
        self.counts = defaultdict(int)
        self.last_price = 10

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        if self.last_price is not None:
            c = self.counts[self.last_price]
            q = self.q_values[self.last_price]

            self.q_values[self.last_price] = q + (last_profit - q) / (c + 1)
            self.counts[self.last_price] += 1

        if random.random() < self.epsilon:
            price = random.uniform(1, 80)
        else:
            price = max(self.q_values, key=self.q_values.get, default=10)

        self.last_price = price
        return price
