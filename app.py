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
    return f"""
    <div style='
        font-size: 2.5em; 
        text-align: center; 
        margin-top: 20%; 
        font-family: Arial, sans-serif;
        color: #333;'>
        Result: <strong>{result}</strong>
        <br><a href="/" style="text-decoration: none; color: #0078d7;">Go Back</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
