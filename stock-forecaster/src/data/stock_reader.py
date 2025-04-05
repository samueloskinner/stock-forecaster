import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockReader:
    def __init__(self, ticker="MSFT"):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_latest_price(self):
        """Fetch the latest closing price"""
        data = self.stock.history(period="1d")
        return data['Close'].iloc[-1]

    def fetch_data(self, start_date=None, end_date=None):
        """Retrieve historical stock data"""
        if not start_date:
            start_date = datetime.now() - timedelta(days=365)
        if not end_date:
            end_date = datetime.now()
            
        data = self.stock.history(start=start_date, end=end_date)
        return data[['Close']]