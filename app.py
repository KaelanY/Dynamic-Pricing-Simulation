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

    def step(self, price, shock_prob, magnitude):
        self.round += 1

        shock_occured = False

        if random.random() < shock_prob:
            self.shock(magnitude)
            shock_occured = True

        quantity = self.demand(price)
        revenue = price*quantity

        return revenue, quantity, shock_occured
    

if "engine" not in st.session_state:
    st.session_state.engine = MarketEngine(100, 1)

engine = st.session_state.engine

st.title("Market Simulation")

price = st.slider("Price", 0.0, 100.0, 1.0)
shock_prob = st.slider("Shock Probability", 0.0, 1.0, 0.1)
magnitude = st.slider("Shock Magnitude", 0.0, 1.0, 0.1)

if st.button("Next Time Step"):
    revenue, quantity, shock = engine.step(price, shock_prob, magnitude)

    st.write(f"Round: {engine.round}")
    st.write(f"Quantity: {quantity:.2f}")
    st.write(f"Revenue: {revenue:.2f}")
    st.write(f"intercept: {engine.intercept:.2f}")
    st.write(f"slope: {engine.slope:.2f}")

    if shock:
        st.warning("Shock occurred!")