from pydantic import BaseModel

import joblib
import numpy as np

model = joblib.load("artifacts/model.pkl")

class WineInput(BaseModel):
    features: list[float]

def predict(payload: WineInput):
    data = np.array(payload.features).reshape(1, -1)
    return model.predict(data)[0]
