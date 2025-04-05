import unittest
from src.data.stock_reader import StockReader

class TestStockReader(unittest.TestCase):

    def setUp(self):
        self.stock_reader = StockReader()

    def test_get_latest_price(self):
        price = self.stock_reader.get_latest_price("MSFT")
        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)

    def test_fetch_data(self):
        historical_data = self.stock_reader.fetch_data("MSFT", "2022-01-01", "2022-12-31")
        self.assertIsInstance(historical_data, list)
        self.assertGreater(len(historical_data), 0)

if __name__ == '__main__':
    unittest.main()