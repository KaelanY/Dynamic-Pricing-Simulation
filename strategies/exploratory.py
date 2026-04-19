import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.baseline = 10
        self.last_price = 10
        self.best_price = 10
        self.best_profit = float("-inf")

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)
        
        if last_profit > self.best_profit:
            self.best_profit = last_profit
            self.best_price = self.last_price
            self.baseline = self.best_price

        if random.random() < 0.15:
            price = random.uniform(1, 80)
        else:
            price = self.baseline + random.uniform(-1, 1)

        price = max(0.1, price)
        self.last_price = price

        return price
