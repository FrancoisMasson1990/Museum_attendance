from fastapi import APIRouter
from models.schemas import AttendancePredictionResponse, Population
import numpy as np
import models.linear_regression as linear_reg

app_museum_predict_v1 = APIRouter()

@app_museum_predict_v1.post('/',
                            tags=["Predictions"],
                            response_model=AttendancePredictionResponse,
                            description="Get a prediction of attendance based on City Population")
async def get_prediction(population: Population):
    response = dict(population)['data']
    data = np.array([response]).reshape(-1, 1)
    prediction = linear_reg.model.predict(data).tolist()
    if prediction:
        return {"prediction": int(prediction[0][0])}
    return {"prediction": -1}
    