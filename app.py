import flask

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"  # Something secure


@app.route("/")
def index():
    return flask.render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
