from prophet import Prophet
import pandas as pd

class StockForecaster:
    def __init__(self):
        self.model = Prophet(daily_seasonality=True)
        
    def prepare_data(self, stock_data):
        """Prepare data for Prophet format"""
        df = stock_data.reset_index()
        df.columns = ['ds', 'y']
        return df
        
    def train(self, stock_data):
        """Train the forecasting model"""
        df = self.prepare_data(stock_data)
        self.model.fit(df)
        
    def forecast(self, days=30):
        """Generate forecast for specified number of days"""
        future_dates = self.model.make_future_dataframe(periods=days)
        forecast = self.model.predict(future_dates)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]