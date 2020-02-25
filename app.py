from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Published using Azure CI/CD pipeline</h1>"
