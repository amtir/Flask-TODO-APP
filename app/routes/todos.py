from flask import Blueprint, redirect, render_template, request, url_for

from app.services.todo_service import complete_todo, create_todo, delete_todo, edit_todo, get_todos

bp = Blueprint("todos", __name__)


@bp.route("/")
def root():
    return render_template("index.html", todo_list=get_todos())


@bp.route("/add", methods=["POST"])
def add():
    create_todo(request.form.get("title"))
    return redirect(url_for("todos.root"))


@bp.route("/update", methods=["POST"])
def update():
    edit_todo(request.form.get("hiddenField"), request.form.get("inputField"))
    return redirect(url_for("todos.root"))


@bp.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for("todos.root"))


@bp.route("/complete/<int:todo_id>", methods=["POST"])
def complete(todo_id):
    complete_todo(todo_id)
    return redirect(url_for("todos.root"))
