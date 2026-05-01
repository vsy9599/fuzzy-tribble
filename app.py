from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Check F1 3 way merge branch!"

if __name__ == "__main__":
    app.run(debug=True)
