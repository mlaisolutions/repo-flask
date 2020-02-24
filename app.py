from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Published using Axure CI/CD pipeline</h1>"
