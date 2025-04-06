from prophet import Prophet
import pandas as pd
from typing import Optional

class StockForecaster:
    """A class to forecast stock prices using Prophet."""
    
    def __init__(self):
        """Initialize the forecaster with default Prophet settings."""
        self.model = Prophet(
            daily_seasonality=True,
            weekly_seasonality=True,
            yearly_seasonality=True
        )
        
    def train(self, data: pd.DataFrame) -> None:
        """
        Train the Prophet model.
        
        Args:
            data (pd.DataFrame): Training data with 'ds' and 'y' columns
        """
        self.model.fit(data)
        
    def forecast(self, days: int = 30) -> pd.DataFrame:
        """
        Generate forecast for specified number of days.
        
        Args:
            days (int): Number of days to forecast
            
        Returns:
            pd.DataFrame: Forecast results
        """
        future = self.model.make_future_dataframe(periods=days)
        forecast = self.model.predict(future)
        return forecast