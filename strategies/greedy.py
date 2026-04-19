from .base import BaseStrategy

class GreedyStrategy(BaseStrategy):
    def __init__(self, price=10):
        self.price = price

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        if last_profit > 0:
            self.price *= 1.01
        else:
            self.price *= 0.99

        return self.price