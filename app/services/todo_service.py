from app.repositories.todo_repository import (
    add_todo,
    list_todos,
    mark_complete,
    remove_todo,
    update_todo_title,
)


def get_todos():
    return list_todos()


def next_todo_id():
    todos = list_todos()
    if not todos:
        return 1
    return max(item.get("id", 0) for item in todos) + 1


def create_todo(raw_title):
    title = (raw_title or "").strip()
    if not title:
        return False
    add_todo(title=title, todo_id=next_todo_id())
    return True


def edit_todo(raw_id, raw_title):
    title = (raw_title or "").strip()
    if not title:
        return False

    try:
        todo_id = int(raw_id)
    except (TypeError, ValueError):
        return False

    return bool(update_todo_title(todo_id, title))


def delete_todo(todo_id):
    return bool(remove_todo(todo_id))


def complete_todo(todo_id):
    return bool(mark_complete(todo_id))
