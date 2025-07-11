import json
from pathlib import Path

import pandas as pd
from joblib import load
from django.conf import settings


class ModelWrapper:
    def __init__(
        self,
        model_path: str | Path = settings.MODEL_PATH,
        features_path: str | Path = settings.FEATURES_PATH,
    ):
        self.model = load(Path(model_path))
        with open(Path(features_path), "rb") as f:
            self.features = json.load(f)

    def _prepare_input(self, data: dict) -> pd.DataFrame:
        """
        Transforms the categorical attributes to the canonical one-hot encoding form
        and aligns the input with the features.
        """
        df = pd.DataFrame([data])  # more readable than as_dict() + processing
        df = pd.get_dummies(df)
        df = df.reindex(columns=self.features, fill_value=0)
        return df

    def predict(self, data: dict) -> float:
        """
        Predicts the price of a house. Assumes that data is in the right format.

        Accepts data in the following format::

            {
                longitude: -122.64
                latitude: 38.01
                housing_median_age: 36.0
                total_rooms: 1336.0
                total_bedrooms: 258.0
                population: 678.0
                households: 249.0
                median_income: 5.5789
                ocean_proximity: 'NEAR OCEAN'
            }
        """

        df = self._prepare_input(data)
        return float(self.model.predict(df)[0])


model = ModelWrapper()
