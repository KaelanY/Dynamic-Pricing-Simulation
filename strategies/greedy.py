from .base import BaseStrategy

class GreedyStrategy(BaseStrategy):
    def __init__(self, price=50.0):
        self.price = float(price)
        self.last_profit = None
        self.direction = 1
        self.step_size = 10.0
        self.streak = 0

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        if self.last_profit is not None:
            if last_profit > self.last_profit:
                self.streak += 1
                self.step_size = min(self.step_size * 1.5, 20.0)
            else:
                self.direction *= -1
                self.streak = 0
                self.step_size = max(self.step_size * 0.5, 1.0)

        self.price += self.direction * self.step_size
        self.price = max(1.0, min(100.0, self.price))

        self.last_profit = last_profit
        return self.price
