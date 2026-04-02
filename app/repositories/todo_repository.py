from app.extensions import db, todo_query


def list_todos():
    return db.all()


def add_todo(title, todo_id):
    db.insert({"id": todo_id, "title": title, "complete": False})


def update_todo_title(todo_id, title):
    return db.update({"title": title}, todo_query.id == todo_id)


def remove_todo(todo_id):
    return db.remove(todo_query.id == todo_id)


def mark_complete(todo_id):
    return db.update({"complete": True}, todo_query.id == todo_id)
