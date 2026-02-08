from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with open("file.txt", "w") as f:
            f.write(
                f"The name is {request.form['name']} and the email is {request.form['email']}"
            )
        return render_template("index.html")
    else:
        return render_template("index.html")


app.run(debug=True)
