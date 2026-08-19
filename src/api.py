from dataclasses import field

from fastapi import FastAPI,HTTPException
from src import database, workouts
from pydantic import BaseModel,Field

from src.database import search_workout_max_weight, search_workout_min_weight

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
@app.get("/workouts/id/{workout_id}")
def get_workout(workout_id: int):
    all_workouts = database.get_workouts()
    if any(workout_id == workout[0] for workout in all_workouts):
        return database.get_workout_by_id(workout_id)
    raise HTTPException(status_code=404, detail="Workout not found.")
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


@app.delete("/workouts/id/{workout_id}")
def delete_workout(workout_id: int):
    all_workouts = database.get_workouts()
    if any(workout_id == workout[0] for workout in all_workouts):
        return database.delete_workout(workout_id)
    raise HTTPException(status_code=404, detail="Workout not found.")
@app.put("/workouts/id/{workout_id}")
def put_workout(workout_id: int, column: str, value):
    all_workouts = database.get_workouts()
    if any(workout_id == workout[0] for workout in all_workouts):
        return [
            database.update_workout(
                workout_id,
                column,
                value
            )
        ]
    raise HTTPException(status_code=404, detail="Workout not found.")

@app.get("/workouts/search")
def get_workout(workout_name: str):
    return database.search_workout_by_name(workout_name)

@app.get("/workouts/filter")
def get_workout_filter(choose: str,value: int):
    if choose == "max":
        return search_workout_max_weight(value)
    if choose == "min":
        return search_workout_min_weight(value)
    raise HTTPException(status_code=404, detail="Workout not found.")

@app.get("/workouts/sort")
def get_workout_sort(choose: str):
    if choose == "asc":
        return database.sort_workout_asc()
    if choose == "desc":
        return database.sort_workout_desc()
    raise HTTPException(status_code=404, detail="Workout not found.")

@app.get("/workouts/stats")
def get_workout_stats():
    return database.get_workouts_stats()
@app.get("/workouts/latest")
def get_latest_workout():
    return database.get_latest_workout()