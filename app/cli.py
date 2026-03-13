import click
from distro import name
from app.tracker import HabitTracker
from app.storage import load_habits, save_habits
from app.analytics import longest_streak_all, longest_streak


tracker = HabitTracker()
tracker.habits = load_habits()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name")
@click.argument("periodicity")
def add(name, periodicity):
    tracker.add_habit(name, periodicity)
    save_habits(tracker.habits)
    click.echo(f"Habit '{name}' added.")


@cli.command()
@click.argument("name")
@click.option("--date", help="Date in YYYY-MM-DD format")
def check(name, date=None):
    tracker.check_off_habit(name, date=date)
    save_habits(tracker.habits)
    click.echo(f"Habit '{name}' completed.")


@cli.command()
@click.option("--periodicity", help="Filter habits by periodicity (daily or weekly)")
def list(periodicity):
    habits = tracker.get_habits()

    if periodicity:
        habits = [h for h in habits if h.periodicity == periodicity]

    for habit in habits:
        click.echo(f"{habit.name} ({habit.periodicity})")


@cli.command()
def stats():

    habits = tracker.get_habits()

    daily = [h for h in habits if h.periodicity == "daily"]
    weekly = [h for h in habits if h.periodicity == "weekly"]

    click.echo("\nHabit Statistics\n")

    click.echo(f"Total habits: {len(habits)}")
    click.echo(f"Daily habits: {len(daily)}")
    click.echo(f"Weekly habits: {len(weekly)}")

    click.echo(f"\nLongest streak overall: {longest_streak_all(habits)}")

    click.echo("\nLongest streak per habit:")

    for habit in habits:
        click.echo(f"{habit.name}: {longest_streak(habit)}")


@cli.command()
@click.argument("name")
def delete(name):
    """Delete a habit"""

    if tracker.delete_habit(name):
        save_habits(tracker.habits)
        click.echo(f"Habit '{name}' deleted.")
    else:
        click.echo("Habit not found.")