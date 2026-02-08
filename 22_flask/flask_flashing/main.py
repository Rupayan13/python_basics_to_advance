from flask import Flask, render_template, flash

app = Flask(__name__)

app.secret_key = "huiodhwivuonwnvbnqivhnqeinvn"


@app.route("/")
def login():
    return render_template("index.html")


@app.route("/logout")
def logout():
    flash("You have been logged out!", "success")
    return render_template("index.html")


app.run(debug=True)
