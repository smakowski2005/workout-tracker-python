from fastapi import FastAPI
from src import database
import datetime
from pydantic import BaseModel

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
    return [
        database.get_workout_by_id(workout_id)
    ]
class Workout(BaseModel):
    cwiczenie: str
    ciezar: int
    powtorzenia: int
    serie: int
@app.post("/workouts")
def post_workout(workout: Workout):
    workout={
            "cwiczenie": workout.cwiczenie,
            "ciezar": workout.ciezar,
            "powtorzenia": workout.powtorzenia,
            "serie": workout.serie,
            "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    database.add_workout(workout)

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    return [
        database.delete_workout(workout_id)
    ]
@app.put("/workouts/{workout_id}")
def put_workout(workout_id: int, column: str, value):
    return [
        database.update_workout(
            workout_id,
            column,
            value
        )
    ]