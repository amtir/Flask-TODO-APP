# Flask TODO App

A lightweight TODO web application built with **Flask** and **TinyDB**. This project demonstrates a simple CRUD-style workflow for tasks: users can add tasks, edit existing task text, mark tasks as complete, and delete tasks from a browser-based interface. The UI is rendered server-side with Jinja2 and styled with W3.CSS plus Font Awesome icons. 

---

## Project Overview

This app is designed as a beginner-friendly example of a Python web application with persistent local storage.

At a high level:

- **Backend framework:** Flask
- **Database:** TinyDB (JSON file-backed)
- **Template engine:** Jinja2 (`templates/index.html`)
- **Persistence file:** `db.json`

When the app starts, it opens `db.json` through TinyDB. Each task is stored as a dictionary with this structure:

- `id` (integer): deterministic, incrementing task ID
- `title` (string): task text entered by user
- `complete` (boolean): completion status

---

## Features

- Add a new task
- View all tasks on the home page
- Edit an existing task via popup form
- Mark a task as complete
- Delete a task
- Persist tasks between restarts using TinyDB (`db.json`)
- Live date/time display in the UI (updated every second in JavaScript)

---

## Repository Structure

```text
Flask-TODO-APP/
├── app.py                  # Flask app, routes, and TinyDB logic
├── db.json                 # TinyDB data file
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Jinja2 template and front-end behavior
└── screenshot/             # Project screenshots
```

---

## Requirements

- Python 3.9+ (recommended)
- `pip` package manager

---

## Setup Instructions

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd Flask-TODO-APP
```

### 2) Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Web Application

### Option A: Run directly with Python

```bash
python app.py
```

The application starts Flask's development server (with `debug=True`) and is typically available at:

- http://127.0.0.1:5000/

### Option B: Run with Flask CLI

```bash
# macOS / Linux
export FLASK_APP=app.py
flask run

# Windows (PowerShell)
$env:FLASK_APP = "app.py"
flask run
```

Then open:

- http://127.0.0.1:5000/

---

## How the Application Works (Component-by-Component)

## 1) Application bootstrap (`app.py`)

- Creates the Flask app instance.
- Initializes TinyDB with `db = TinyDB('db.json')`.
- Defines `_next_todo_id()` to assign predictable, collision-resistant IDs by using `max(existing_ids) + 1`.

Why deterministic IDs matter:
- Random IDs can collide and may affect multiple records during update/delete operations.
- Incrementing IDs ensure route actions target a single intended task.

## 2) Data model in TinyDB

Each task is saved like:

```python
{'id': 1, 'title': 'Buy groceries', 'complete': False}
```

TinyDB stores records in `db.json`, so data persists after application restart.

## 3) Routes and request flow

### `GET /` — Home page
- Reads all tasks (`db.all()`).
- Renders `templates/index.html` with `todo_list`.

### `POST /add` — Create task
- Reads `title` from submitted form.
- Trims whitespace.
- If empty, redirects back without insertion.
- Otherwise inserts a new task with:
  - next ID
  - title text
  - `complete=False`
- Redirects to `/`.

### `POST /update` — Edit task title
- Reads:
  - `inputField` (new task text)
  - `hiddenField` (task ID)
- Updates matched TinyDB record by `id`.
- Redirects to `/`.

### `GET /delete/<int:todo_id>` — Delete task
- Removes the record whose `id` equals `todo_id`.
- Redirects to `/`.

### `GET /complete/<int:todo_id>` — Mark complete
- Updates task `complete` value to `True`.
- Redirects to `/`.

## 4) Template rendering (`templates/index.html`)

The template loops through `todo_list` and conditionally renders:

- **Incomplete tasks** with normal styling and a complete button.
- **Completed tasks** with green styling and strike-through text (`<del>`).

For each task, the template provides action controls:

- Complete (`/complete/<id>`) for incomplete items
- Edit (opens popup modal with current title pre-filled)
- Delete (`/delete/<id>`)

## 5) Front-end behavior

JavaScript in `index.html` handles:

- **Live date/time** display (`setInterval` every second)
- **Edit popup open** (`openPopup(id)`) that:
  - reads task text from DOM
  - pre-populates edit form
  - sets hidden ID input
- Form submission to `/update`

---

## Usage Guide

1. Open the app in your browser.
2. Type a task in **Add Your Task Here** and click `+`.
3. Click ✓ to mark a task complete.
4. Click the pencil icon to edit a task title, then click **Update**.
5. Click the trash icon to delete a task.

---

## Notes and Limitations

- This app uses Flask's development server; do not use it directly for production.
- `debug=True` is enabled when running `python app.py`.
- There is no user authentication; all tasks are shared in the same local database file.
- Route actions for complete/delete are triggered by `GET`; in larger production apps these are typically `POST`/`PATCH`/`DELETE`.

---

## Troubleshooting

### `ModuleNotFoundError` errors
Install dependencies again in your active virtual environment:

```bash
pip install -r requirements.txt
```

### `greenlet` build errors on Python 3.12 (Windows)
If installation fails while compiling `greenlet==2.0.2`, upgrade to the repo's current dependency set and reinstall:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This repository pins `greenlet==3.0.3`, which provides Python 3.12 compatible wheels.

### Port 5000 already in use
Run on another port:

```bash
flask run --port 5001
```

### Data reset
If you want a clean task list, stop the app and clear/reset `db.json` contents.

---

## Future Improvements (Optional)

- Add validation for update input (avoid empty titles on edit).
- Add ability to toggle task completion back to incomplete.
- Use CSRF protection and Flask-WTF forms.
- Refactor routes to use HTTP verbs more semantically.
- Add unit/integration tests.
- Add Docker support and production WSGI server configuration.

---

## Screenshots

![Home](screenshot/Home.png)

![Task Creation](screenshot/Task_creation.png)

![Task Update](screenshot/UpdateTodo.png)

![Update/Delete](screenshot/update_delete.png)
