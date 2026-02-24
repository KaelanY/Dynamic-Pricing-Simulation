import yfinance as yf
import pandas as pd
import streamlit as st

def get_market_shock_factor(ticker):
    """
    Fetches real-world stock data and calculates a shock multiplier 
    based on the most recent daily percentage change.
    """
    try:
        # downloads the last 5 days of data
        stock = yf.Ticker(ticker)
        df = stock.history(period="5d")
        
        if df.empty or len(df) < 2:
            return 1.0, "No data found for ticker."

        # daily % change (Current Close - Previous Close) / Previous Close
        current_price = df['Close'].iloc[-1]
        prev_price = df['Close'].iloc[-2]
        change_pct = (current_price - prev_price) / prev_price
        
        # Multiplier: 1.0 means no change
        #0.95 means 5% market drop
        shock_multiplier = 1.0 + change_pct
        
        return shock_multiplier, f"Success: {ticker} changed by {change_pct:.2%}"
        
    except Exception as e:
        return 1.0, f"Error fetching data: {str(e)}"
