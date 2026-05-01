from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Check F1 branch!"

if __name__ == "__main__":
    app.run(debug=True)
