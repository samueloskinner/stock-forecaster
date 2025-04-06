# README.md

# Stock Forecaster

A Python library to fetch Microsoft stock prices and forecast them for the next 30 days using Prophet.

## Features

- Fetch the latest stock price of Microsoft.
- Retrieve historical stock data.
- Train a forecasting model.
- Predict stock prices for the next 30 days.
- Utility functions for data processing and visualization.

## Installation

```bash
pip install -e .
```

## Usage

```python
from stockforecaster.data.stock_reader import StockReader
from stockforecaster.models.forecaster import StockForecaster

# Initialize reader
reader = StockReader(ticker="MSFT")

# Get historical data
data = reader.fetch_data()

# Train and forecast
forecaster = StockForecaster()
forecaster.train(data)
forecast = forecaster.forecast(days=30)

# Plot the forecast
forecaster.model.plot(forecast)
import matplotlib.pyplot as plt
plt.show()
```

## Docker Usage

```bash
docker build -t stock-forecaster .
docker run stock-forecaster
```

## Running Tests

To run the unit tests for the library, use:

```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

MIT