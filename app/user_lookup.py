import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    # Look up a user profile by name.
    name = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % name)
    row = cur.fetchone()
    return {"user": row}

@app.route("/run")
def run_command():
    import os
    cmd = request.args.get("cmd", "ls")
    return {"output": os.popen(cmd).read()}
