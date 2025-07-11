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

    def prepare_input(self, data: dict) -> pd.DataFrame:
        df = pd.DataFrame([data])  # more readable than as_dict() + processing
        df = pd.get_dummies(df)
        df = df.reindex(columns=self.features, fill_value=0)
        return df

    def predict(self, data: dict) -> float:
        df = self.prepare_input(data)
        return float(self.model.predict(df)[0])


model = ModelWrapper()
