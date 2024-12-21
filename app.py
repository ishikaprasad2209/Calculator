from flask import Flask, render_template, request
from logic import calculate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_route():
    expression = request.form["expression"]
    result = calculate(expression)
    return f"<div style='font-size: 2em; text-align: center; margin-top: 20%;'>Result: <strong>{result}</strong></div>"

if __name__ == "__main__":
    app.run(debug=True)
