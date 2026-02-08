from flask import Flask, render_template

# app = Flask(
#     __name__, static_url_path="/public"
# )  # This will change the static url path

app = Flask(
    __name__, static_folder="assests", static_url_path="/static"
)  # This will change the staic folder location


@app.route("/")
def home():
    return render_template("index.html")


app.run(debug=True)
