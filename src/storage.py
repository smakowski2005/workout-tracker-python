import json

def load_workouts():
    try:
        with open('/Users/sebastian/PycharmProjects/PythonProject1/data/workouts.json') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def save_workouts(workouts):
    with open('/Users/sebastian/PycharmProjects/PythonProject1/data/workouts.json', 'w') as outfile:
        json.dump(workouts, outfile)
