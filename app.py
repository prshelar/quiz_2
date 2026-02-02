from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

ADMIN_PASSWORD = "love123"  # change if you want

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    entry = {
        "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "answers": data
    }

    try:
        with open("responses.json", "r") as f:
            existing = json.load(f)
    except:
        existing = []

    existing.append(entry)

    with open("responses.json", "w") as f:
        json.dump(existing, f, indent=2)

    return {"status": "saved"}

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form["password"] != ADMIN_PASSWORD:
            return "Wrong password"

    try:
        with open("responses.json") as f:
            data = json.load(f)
    except:
        data = []

    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)