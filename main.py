from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class Item(BaseModel):
    size: float
    nb_bedrooms: int
    has_garden: int

app = FastAPI()

model = joblib.load("regression.joblib")

@app.post("/predict")
async def predict_post(data: Item):
    return {"y_pred": float(model.predict([[data.size, data.nb_bedrooms, data.has_garden]]))}
