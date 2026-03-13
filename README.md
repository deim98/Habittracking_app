# Habit Tracking CLI Application

## Overview

This project is a **Command Line Interface (CLI) Habit Tracking Application** built in Python.
It allows users to create habits, record completions, and analyze habit streaks. The application supports **daily and weekly habits**, tracks completion history, and provides simple analytics such as the longest streak.

The project demonstrates:

* Object-Oriented Programming (OOP)
* Functional programming concepts for analytics
* Command Line Interface design
* Unit testing with pytest
* Data persistence using JSON

---

## Features

The application provides the following functionality:

* Add new habits
* Delete existing habits
* Check off a habit completion
* List all tracked habits
* Calculate analytics such as longest streaks
* Load predefined habits with completion history
* Persist habit data using JSON storage

Habits can be defined with the following periodicities:

* **Daily**
* **Weekly**

---

## Project Structure

```
Habittracking_app/
│
├── app/
│   ├── habit.py        # Habit class and logic
│   ├── tracker.py      # HabitTracker management class
│   ├── analytics.py    # Analytical functions (streak calculations)
│   ├── storage.py      # JSON persistence layer
│   └── cli.py          # Command Line Interface commands
│
├── tests/
│   ├── test_habit.py
│   ├── test_tracker.py
│   └── test_analytics.py
│
├── main.py             # Application entry point
├── habits.json         # Stored habit data
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/deim98/habittracking_app.git
cd habittracking_app
```

### 2. Create a virtual environment

```
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

All commands are executed through the CLI.

### Show available commands

```
python main.py --help
```

---

### Add a new habit

```
python main.py add "Drink Water" daily
```

---

### Check off a habit

```
python main.py check "Drink Water"
```

Optional date:

```
python main.py check "Drink Water" --date 2026-03-01
```

---

### List all habits

```
python main.py list
```

Example output:

```
Drink Water (daily)
Exercise (weekly)
Meditate (daily)
```

---

### View statistics

```
python main.py stats
```

Example output:

```
Longest streak: 7
```

---

## Predefined Habits

The application loads **five predefined habits with four weeks of completion data** to demonstrate analytics functionality. These include both daily and weekly habits.

---

## Testing

Unit tests are implemented using **pytest**.

Run the test suite:

```
pytest
```

The tests cover:

* Habit creation and completion tracking
* HabitTracker functionality
* Analytics calculations such as streaks

---

## Analytics Functions

The analytics module provides pure functions to analyze habit data, including:

* Longest streak for a specific habit
* Longest streak across all habits
* Habit completion analysis based on periodicity

These functions operate independently of the CLI and tracker logic.

---

## Data Storage

Habit data is stored in a **JSON file (`habits.json`)**.
Each habit stores:

* Name
* Periodicity
* Completion timestamps

This allows the application to persist data between sessions.

---

## Future Improvements

Potential improvements include:

* Graphical user interface
* Web-based dashboard
* Database storage (SQLite/PostgreSQL)
* Reminder notifications
* Habit performance visualizations

---

## Author

Dame Obaseki

---

## License

This project is for educational purposes.
