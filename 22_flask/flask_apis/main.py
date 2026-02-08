from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    marks = {
        "Rupayan": 90,
        "Rafi": 85,
        "Rafiq": 92,
        "Rupali": 88,
        "Prothom": 95,
    }
    return jsonify(marks)


app.run(debug=True)
