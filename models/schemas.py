from pydantic import BaseModel


class Population(BaseModel):
    data: int


class AttendancePredictionResponse(BaseModel):
    prediction: int