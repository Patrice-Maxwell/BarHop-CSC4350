import os
import flask
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://luluzeugoxqaba:f082d0f1f1f01321bfe2e94fd176374166edda647252c2e795b5a9a189970816@ec2-107-23-135-132.compute-1.amazonaws.com:5432/d3v8dftmvr631l"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Staff(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    employee_first_name = db.Column(db.String(120), nullable=False)
    employee_last_name = db.Column(db.String(120), nullable=False)
    employee_email = db.Column(db.String(180), nullable=False)
    employee_availability = db.Column(db.String(180), nullable=True)
    password = db.Column(db.String(180), nullable=True)


db.create_all()


@app.route("/")
def main():

    new_employee = Staff(
        employee_first_name="test_rice",
        employee_last_name="test_maxwell",
        employee_email="test_group@project.com",
        employee_availability="test never",
    )
    db.session.add(new_employee)
    db.session.commit()
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
