import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime
from app.habit import Habit


def test_create_habit():

    habit = Habit("Drink Water", "daily")

    assert habit.name == "Drink Water"
    assert habit.periodicity == "daily"
    assert habit.completions == []


def test_check_off_habit():

    habit = Habit("Exercise", "weekly")

    habit.check_off()

    assert len(habit.completions) == 1


def test_to_dict():

    habit = Habit("Read", "daily")

    habit.check_off(datetime(2026, 2, 1))

    habit_dict = habit.to_dict()

    assert habit_dict["name"] == "Read"
    assert habit_dict["periodicity"] == "daily"
    assert len(habit_dict["completions"]) == 1


def test_from_dict():

    data = {
        "name": "Meditate",
        "periodicity": "daily",
        "created_at": "2026-02-01T08:00:00",
        "completions": ["2026-02-02T08:00:00"]
    }

    habit = Habit.from_dict(data)

    assert habit.name == "Meditate"
    assert habit.periodicity == "daily"
    assert len(habit.completions) == 1