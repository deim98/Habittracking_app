import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tracker import HabitTracker


def test_add_habit():

    tracker = HabitTracker()

    tracker.add_habit("Drink Water", "daily")

    assert "Drink Water" in tracker.habits


def test_get_habits():

    tracker = HabitTracker()

    tracker.add_habit("Exercise", "weekly")

    habits = tracker.get_habits()

    assert len(habits) == 1
    assert habits[0].name == "Exercise"


def test_delete_habit():

    tracker = HabitTracker()

    tracker.add_habit("Read Book", "daily")

    tracker.delete_habit("Read Book")

    assert "Read Book" not in tracker.habits


def test_check_off_habit():

    tracker = HabitTracker()

    tracker.add_habit("Meditate", "daily")

    tracker.check_off_habit("Meditate")

    habit = tracker.habits["Meditate"]

    assert len(habit.completions) == 1
