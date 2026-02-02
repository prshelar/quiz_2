from flask import Flask, render_template, request, redirect, url_for
import json
import os
 
app = Flask(__name__)
 
RESPONSES_FILE = "responses.json"
 
# Load existing responses or create empty list
if not os.path.exists(RESPONSES_FILE):
    with open(RESPONSES_FILE, "w") as f:
        json.dump([], f)
 
@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json  # get JSON data from JS
    if not data:
        return {"status": "error"}, 400
 
    # Load existing responses
    with open(RESPONSES_FILE, "r") as f:
        responses = json.load(f)
 
    # Append new response
    responses.append(data)
 
    # Save back
    with open(RESPONSES_FILE, "w") as f:
        json.dump(responses, f, indent=4)
 
    return {"status": "success"}, 200
 
@app.route("/admin")
def admin():
    with open(RESPONSES_FILE, "r") as f:
        responses = json.load(f)
    return render_template("admin.html", responses=responses)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
