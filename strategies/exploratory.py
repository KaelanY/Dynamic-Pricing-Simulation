import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self, base_price=10):
        self.base_price = base_price

    def choose_price(self, state):
        noise = random.uniform(-3, 3)
        return max(0.1, self.base_price + noise)