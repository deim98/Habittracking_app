from datetime import datetime
from typing import List
from app.habit import Habit


class HabitTracker:
    # Manages a collection of habits, allowing for adding, checking off,
    # and retrieving habits.

    def __init__(self):
        self.habits = {} # Dictionary to store habits by name for easy access


    def add_habit(self, name: str, periodicity: str):
        # Adds a new habit to the tracker.
        habit = Habit(name, periodicity)
        self.habits[name] = habit

    def delete_habit(self, habit_name: str):
        # Deletes a specific habit from the tracker.
        if habit_name in self.habits:
            del self.habits[habit_name]
            return True
        return False


    def check_off_habit(self, habit_name: str, date: datetime = None):
        # Marks a specific habit as completed for a given date and time.
        habit = self.habits.get(habit_name)
        
        if not habit:
            raise ValueError(f"Habit '{habit_name}' not found.")
        
        habit.check_off(date)


    def get_habits(self):
        # Retrieves the list of all habits being tracked.
        return list(self.habits.values())
