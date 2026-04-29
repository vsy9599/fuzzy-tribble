from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from git and local repository!"

if __name__ == "__main__":
    app.run(debug=True)