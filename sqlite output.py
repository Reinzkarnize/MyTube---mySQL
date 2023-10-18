from cs50 import SQL


db = SQL("sqlite:///mytube.db")

playlist_id = db.execute("SELECT * FROM users;")

print(playlist_id)