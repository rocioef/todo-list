import json
from app.models.task import Task

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    data = [task.to_dict() for task in tasks]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)