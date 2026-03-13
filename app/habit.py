from datetime import datetime
from typing import List


class Habit:
    # Represents a habit with a defined periodicity and completion history.

    def __init__(self, name: str, periodicity: str, created_at=None, completions=None):
        self.name = name
        self.periodicity = periodicity  # e.g., 'daily', 'weekly', 'monthly'
        self.created_at = created_at if created_at else datetime.now()
        self.completions = completions if completions else []

    def check_off(self, date=None):
        # Marks the habit as completed for a specific date and time.
        if date is None:
            completion_date = datetime.now()
        elif isinstance(date, str):
            completion_date = datetime.fromisoformat(date)
        elif isinstance(date, datetime):
            completion_date = date
        else:
            raise ValueError("Invalid date format. Use datetime or ISO string.")
        
        self.completions.append(completion_date)

    def to_dict(
        self,
    ):  # Converts the habit instance into a dictionary format for easy storage and retrieval.
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [completion.isoformat() for completion in self.completions],
        }

    @staticmethod
    def from_dict(data: dict):
        # Creates a Habit instance from a dictionary, facilitating the loading of habit data from storage.
        created_at = datetime.fromisoformat(data["created_at"])
        completions = [
            datetime.fromisoformat(completion) for completion in data["completions"]
        ]
        return Habit(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=created_at,
            completions=completions,
        )
