import streamlit as st
import random

class MarketEngine:
    def __init__(self, intercept, slope):
        self.round = 0
        self.intercept = intercept
        self.slope = slope

#function to calculate the quantity demanded at a certain price, demand function is Q = a - b*price
    def demand(self, price):
        quantity = max(self.intercept - self.slope*price, 0)
        return quantity

#these are the economic shocks, it changes the coefficients of the demand curve, slope is inversely proportional to intercept change
    def shock(self, magnitude):
        shock = random.uniform(-magnitude, magnitude)
        self.intercept *= 1+shock
        self.slope *= 1-shock

    def step(self, price):
        self.round += 1
        quantity = self.demand(price)
        revenue = price*quantity
        return revenue