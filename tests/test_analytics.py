import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime
from app.analytics import longest_streak, longest_streak_all, habits_by_periodicity
from app.habit import Habit


def test_longest_streak_daily():

    habit = Habit("Drink Water", "daily")

    habit.completions = [
        datetime(2026, 2, 1),
        datetime(2026, 2, 2),
        datetime(2026, 2, 3),
    ]

    assert longest_streak(habit) == 3


def test_longest_streak_weekly():

    habit = Habit("Exercise", "weekly")

    habit.completions = [
        datetime(2026, 2, 1),
        datetime(2026, 2, 8),
        datetime(2026, 2, 15),
    ]

    assert longest_streak(habit) == 3


def test_longest_streak_all():

    habit1 = Habit("Drink Water", "daily")
    habit1.completions = [
        datetime(2026, 2, 1),
        datetime(2026, 2, 2),
        datetime(2026, 2, 3),
    ]

    habit2 = Habit("Exercise", "weekly")
    habit2.completions = [
        datetime(2026, 2, 1),
        datetime(2026, 2, 8),
    ]

    assert longest_streak_all([habit1, habit2]) == 3


def test_habits_by_periodicity():

    habit1 = Habit("Drink Water", "daily")
    habit2 = Habit("Exercise", "weekly")
    habit3 = Habit("Read", "daily")

    habits = [habit1, habit2, habit3]

    daily_habits = habits_by_periodicity(habits, "daily")

    assert len(daily_habits) == 2
