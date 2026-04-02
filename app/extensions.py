from tinydb import Query, TinyDB

# Shared app resources
DB_PATH = "db.json"
db = TinyDB(DB_PATH)
todo_query = Query()
