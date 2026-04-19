import random

class MarketEngine:
    def __init__(self, intercept=100, slope=1):
        self.initial_intercept = intercept
        self.initial_slope = slope
        self.reset()

    def reset(self):
        self.round = 0
        self.intercept = self.initial_intercept
        self.slope = self.initial_slope

    def demand(self, price):
        return max(self.intercept - self.slope * price, 0)

    def maybe_shock(self, shock_prob, magnitude):
        if random.random() < shock_prob:
            shock = random.uniform(-magnitude, magnitude)
            self.intercept *= (1 + shock)
            self.slope *= (1 - shock)
            return True
        return False

    def step(self, price, shock_prob=0.0, magnitude=0.0):
        self.round += 1

        shock = self.maybe_shock(shock_prob, magnitude)

        quantity = self.demand(price)
        revenue = price * quantity

        return {
            "quantity": quantity,
            "revenue": revenue,
            "shock": shock
        }