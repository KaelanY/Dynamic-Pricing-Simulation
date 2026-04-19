import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.prices_tried = []
        self.base_price = 10

    def choose_price(self, state):
        if random.random() < 0.7:
            # explore a wide range
            price = random.uniform(1, 30)
        else:
            # local variation around base
            noise = random.uniform(-5, 5)
            price = self.base_price + noise

        price = max(0.1, price)
        self.prices_tried.append(price)
        self.base_price = sum(self.prices_tried[-10:]) / min(len(self.prices_tried), 10)

        return price
