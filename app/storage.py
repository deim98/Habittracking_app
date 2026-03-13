import json
from app.habit import Habit


DATA_FILE = "data/habits.json"


def save_habits(habits: dict):
    with open(DATA_FILE, "w") as f:
        json.dump({k: v.to_dict() for k, v in habits.items()}, f, indent=2)


def load_habits():
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
            return {k: Habit.from_dict(v) for k, v in data.items()}
    except FileNotFoundError:
        return {}
