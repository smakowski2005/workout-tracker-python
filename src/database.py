import sqlite3
import os

def connect():
    return sqlite3.connect('/Users/sebastian/PycharmProjects/PythonProject1/data/database.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER NOT NULL PRIMARY KEY,
        cwiczenie TEXT,
        ciezar INTEGER,
        powtorzenia INTEGER,
        serie INTEGER,
        data TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_workout(workout):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO workouts VALUES (?,?,?,?,?,?)
    """,
    (
        workout['id'],
        workout['cwiczenie'],
        workout['ciezar'],
        workout['powtorzenia'],
        workout['serie'],
        workout['data']
    ))
    conn.commit()
    conn.close()
def delete_workout(workout_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM workouts WHERE id =?""",
        (workout_id,)
    )
    conn.commit()
    conn.close()
def get_workouts():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
    "SELECT * FROM workouts"
    )
    workouts = cursor.fetchall()
    conn.close()
    return workouts
def delete_database():
    while True:
        answer = input("Czy na pewno? y/n")
        if answer=="y":
            os.remove('/Users/sebastian/PycharmProjects/PythonProject1/data/database.db')
            break
        elif answer=="n":
            break
        else:
            print("blad podaj y lub n")
def get_workout_by_id(workout_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM workouts WHERE id = ?
        """,
        (workout_id,)
    )
    workout = cursor.fetchone()
    conn.close()
    return workout

def update_workout(workout_id, column, value):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        UPDATE workouts
        SET {column} = ?
        WHERE id = ?
        """,
        (value, workout_id)
    )
    conn.commit()
    conn.close()