import numpy as np
import matplotlib.pyplot as plt

def calculate_moving_average(prices, window):
    """Calculate the moving average of a given list of prices."""
    return np.convolve(prices, np.ones(window)/window, mode='valid')

def plot_forecast(dates, actual_prices, forecasted_prices):
    """Plot the actual prices and the forecasted prices."""
    plt.figure(figsize=(10, 5))
    plt.plot(dates, actual_prices, label='Actual Prices', color='blue')
    plt.plot(dates[-len(forecasted_prices):], forecasted_prices, label='Forecasted Prices', color='orange')
    plt.title('Stock Price Forecast')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()