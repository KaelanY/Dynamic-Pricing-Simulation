import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.baseline = 10

    def choose_price(self, state):
        history = state.get("history", [])

        if len(history) > 5:
            best = max(history, key=lambda x: x[1])
            best_price = best[0]
            self.baseline = best_price

        if random.random() < 0.2:
            price = random.uniform(1, 300)
        else:
            price = self.baseline + random.uniform(-2, 2)

        return max(0.1, price)
