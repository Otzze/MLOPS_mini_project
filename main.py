from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict_get():
    return {"y_pred": 2}
