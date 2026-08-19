import sqlite3
import os

def connect():
    return sqlite3.connect('/Users/sebastian/PycharmProjects/PythonProject1/data/database.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
def search_workout_by_name(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM workouts
        WHERE cwiczenie LIKE ?
        """,
        (f"%{name}%",)
    )
    workout = cursor.fetchall()
    conn.close()
    return workout

def search_workout_max_weight(max_weight):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM workouts
        WHERE ciezar <= ?
        """,
        (max_weight,)
    )
    workout = cursor.fetchall()
    conn.close()
    return workout

def search_workout_min_weight(min_weight):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM workouts
        WHERE ciezar >= ?
        """,
        (min_weight,)
    )
    workout = cursor.fetchall()
    conn.close()
    return workout

def sort_workout_asc():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM workouts
        ORDER BY cwiczenie ASC"""
    )
    workout = cursor.fetchall()
    conn.close()
    return workout
def sort_workout_desc():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM workouts
        ORDER BY cwiczenie DESC"""
    )
    workout = cursor.fetchall()
    conn.close()
    return workout
def get_workouts_stats():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT COUNT(id),AVG(ciezar),MAX(ciezar) FROM workouts
        """
    )
    stats = cursor.fetchone()
    conn.close()
    return {
        "workouts": stats[0],
        "average weight": round(stats[1],2),
        "max weight": stats[2],
    }

def get_latest_workout():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM workouts
        ORDER BY id DESC LIMIT 1"""
    )
    workout = cursor.fetchall()
    conn.close()
    return workout