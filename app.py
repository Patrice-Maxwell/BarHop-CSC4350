import flask

app = flask.Flask(__name__)


@app.route("/")
def main():
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
