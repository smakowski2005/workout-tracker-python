from fastapi import FastAPI
from src import database

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