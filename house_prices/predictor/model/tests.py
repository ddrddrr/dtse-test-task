from django.test import TestCase

from predictor.model.wrapper import ModelWrapper


class TestModelWrapper(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.wrapper = ModelWrapper()

    def test_prediction_input1(self):
        data = {
            "longitude": -122.64,
            "latitude": 38.01,
            "housing_median_age": 36.0,
            "total_rooms": 1336.0,
            "total_bedrooms": 258.0,
            "population": 678.0,
            "households": 249.0,
            "median_income": 5.5789,
            "ocean_proximity": "NEAR OCEAN",
        }
        expected = 320201.58554044
        result = self.wrapper.predict(data)
        self.assertAlmostEqual(result, expected, places=5)

    def test_prediction_input2(self):
        data = {
            "longitude": -115.73,
            "latitude": 33.35,
            "housing_median_age": 23.0,
            "total_rooms": 1586.0,
            "total_bedrooms": 448.0,
            "population": 338.0,
            "households": 182.0,
            "median_income": 1.2132,
            "ocean_proximity": "INLAND",
        }
        expected = 58815.45033765
        result = self.wrapper.predict(data)
        self.assertAlmostEqual(result, expected, places=5)

    def test_prediction_input3(self):
        data = {
            "longitude": -117.96,
            "latitude": 33.89,
            "housing_median_age": 24.0,
            "total_rooms": 1332.0,
            "total_bedrooms": 252.0,
            "population": 625.0,
            "households": 230.0,
            "median_income": 4.4375,
            "ocean_proximity": "<1H OCEAN",
        }
        expected = 192575.77355635
        result = self.wrapper.predict(data)
        self.assertAlmostEqual(result, expected, places=5)
