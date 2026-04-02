from app import create_app


def _client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_mutating_endpoints_reject_get_requests():
    client = _client()

    assert client.get("/add").status_code == 405
    assert client.get("/update").status_code == 405
    assert client.get("/delete/1").status_code == 405
    assert client.get("/complete/1").status_code == 405


def test_mutating_endpoints_accept_post_requests(monkeypatch):
    client = _client()

    monkeypatch.setattr("app.routes.todos.create_todo", lambda _title: True)
    monkeypatch.setattr("app.routes.todos.edit_todo", lambda _id, _title: True)
    monkeypatch.setattr("app.routes.todos.delete_todo", lambda _id: True)
    monkeypatch.setattr("app.routes.todos.complete_todo", lambda _id: True)

    assert client.post("/add", data={"title": "Task"}).status_code == 302
    assert client.post(
        "/update", data={"hiddenField": "1", "inputField": "Updated"}
    ).status_code == 302
    assert client.post("/delete/1").status_code == 302
    assert client.post("/complete/1").status_code == 302
