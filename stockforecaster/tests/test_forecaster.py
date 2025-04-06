import unittest
from src.models.forecaster import Forecaster

class TestForecaster(unittest.TestCase):

    def setUp(self):
        self.forecaster = Forecaster()

    def test_train_model(self):
        # Assuming we have some historical data to train on
        historical_data = [100, 101, 102, 103, 104]
        self.forecaster.train_model(historical_data)
        self.assertIsNotNone(self.forecaster.model)

    def test_forecast(self):
        # Assuming the model has been trained
        historical_data = [100, 101, 102, 103, 104]
        self.forecaster.train_model(historical_data)
        forecasted_prices = self.forecaster.forecast(30)
        self.assertEqual(len(forecasted_prices), 30)

if __name__ == '__main__':
    unittest.main()