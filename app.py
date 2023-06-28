import models.linear_regression as linear_reg
from fastapi import FastAPI
from joblib import load
from routes.museum_attendance_predict import app_museum_predict_v1

app = FastAPI(title="Museum Attendance ML",
              description="API for Museum Attendance Based on Population",
              version="1.0")

@app.on_event('startup')
async def load_model():
    linear_reg.model = load('models/museum_tourist.joblib')

app.include_router(app_museum_predict_v1)