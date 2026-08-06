from dataclasses import field

from fastapi import FastAPI,HTTPException
from src import database, workouts
from pydantic import BaseModel,Field
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Workout Tracker API dziala!"
    }
@app.get("/workouts")
def get_workouts():

    return [
        database.get_workouts()
    ]
@app.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    if workout_id not in workouts:
        raise HTTPException(status_code=404, detail="Workout not found.")
    return [
        database.get_workout_by_id(workout_id)
    ]
class Workout(BaseModel):
    cwiczenie: str
    ciezar: int = Field(gt=0)
    powtorzenia: int = Field(gt=0)
    serie: int = Field(gt=0)
@app.post("/workouts")
def post_workout(workout: Workout):
    workout={
            "cwiczenie": workout.cwiczenie,
            "ciezar": workout.ciezar,
            "powtorzenia": workout.powtorzenia,
            "serie": workout.serie,
            "data": workouts.data
        }
    database.add_workout(workout)
    message = "Workout added successfully!"
    return message


@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    if workout_id not in workouts:
        raise HTTPException(status_code=404, detail="Workout not found.")
    return [
        database.delete_workout(workout_id)
    ]
@app.put("/workouts/{workout_id}")
def put_workout(workout_id: int, column: str, value):
    if workout_id not in workouts:
        raise HTTPException(status_code=404, detail="Workout not found.")
    return [
        database.update_workout(
            workout_id,
            column,
            value
        )
    ]