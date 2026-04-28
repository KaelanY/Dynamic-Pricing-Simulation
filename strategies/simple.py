from .base import BaseStrategy

class SimpleStrategy(BaseStrategy):
    def __init__(self, price=10.0, step=2.0):
        self.price = float(price)
        self.step = float(step)
        self.direction = 1  # 1 = increase price, -1 = decrease
        self.last_profit = None

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        # If we have previous info, adjust direction
        if self.last_profit is not None:
            if last_profit < self.last_profit:
                # Profit got worse → reverse direction
                self.direction *= -1

        # Move price
        self.price += self.direction * self.step

        # Keep within bounds
        self.price = max(1.0, min(100.0, self.price))

        # Update memory
        self.last_profit = last_profit

        return self.price
