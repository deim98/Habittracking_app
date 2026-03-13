from datetime import timedelta


def list_all_habits(habits):
    return habits


def habits_by_periodicity(habits, periodicity):
    return [h for h in habits if h.periodicity == periodicity]


def longest_streak(habit):
    if not habit.completions:
        return 0

    sorted_dates = sorted(habit.completions)

    streak = 1
    max_streak = 1

    for i in range(1, len(sorted_dates)):

        delta = sorted_dates[i] - sorted_dates[i - 1]

        if habit.periodicity == "daily" and delta.days == 1:
            streak += 1
        elif habit.periodicity == "weekly" and delta.days == 7:
            streak += 1
        else:
            streak = 1

        max_streak = max(max_streak, streak)

    return max_streak


def longest_streak_all(habits):
    return max(longest_streak(h) for h in habits)
