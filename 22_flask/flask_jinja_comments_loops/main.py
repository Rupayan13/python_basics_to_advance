from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    marks = {
        "Rupayan": 90,
        "Sayan": 80,
        "Sourav": 85,
        "Preet": 95,
    }
    return render_template("index.html", marks=marks)


app.run(debug=True)
