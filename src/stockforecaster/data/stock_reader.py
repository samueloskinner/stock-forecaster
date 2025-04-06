import yfinance as yf
import pandas as pd
from typing import Optional

class StockReader:
    """A class to fetch and prepare stock data for forecasting."""
    
    def __init__(self, ticker: str = "MSFT", period: str = "5y"):
        """
        Initialize the StockReader.
        
        Args:
            ticker (str): Stock ticker symbol (default: "MSFT")
            period (str): Data fetch period (default: "5y")
        """
        self.ticker = ticker
        self.period = period
        
    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch stock data and prepare it for Prophet.
        
        Returns:
            pd.DataFrame: DataFrame with 'ds' (date) and 'y' (close price) columns
        """
        # Fetch data
        ticker = yf.Ticker(self.ticker)
        df = ticker.history(period=self.period)
        
        # Reset index to make date a column
        df = df.reset_index()
        
        # Remove timezone information
        df['Date'] = df['Date'].dt.tz_localize(None)
        
        # Rename columns to Prophet requirements
        df = df.rename(columns={
            'Date': 'ds',
            'Close': 'y'
        })
        
        # Select only required columns
        df = df[['ds', 'y']]
        
        return df