import logging
from logging import error
import os
from dotenv import load_dotenv, find_dotenv
import flask
from flask_login import login_user, LoginManager, current_user, UserMixin
import flask_login
from flask_login.utils import login_required, logout_user
from flask.templating import render_template

from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://luluzeugoxqaba:f082d0f1f1f01321bfe2e94fd176374166edda647252c2e795b5a9a189970816@ec2-107-23-135-132.compute-1.amazonaws.com:5432/d3v8dftmvr631l"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = b"os.getenv('APP_SECRET_KEY')"

db = SQLAlchemy(app)


class Staff(db.Model, UserMixin):
    task_id = db.Column(db.Integer, primary_key=True)
    employee_first_name = db.Column(db.String(120), nullable=False)
    employee_last_name = db.Column(db.String(120), nullable=False)
    employee_email = db.Column(db.String(180), nullable=False)
    employee_availability = db.Column(db.String(180), nullable=True)
    # password = db.Column(db.String(180), nullable=True)

    def get_id(self):
        return self.task_id


db.create_all()

# What is this function for?
def getDB():

    items = Staff.query.all()

    first_name_list = []
    last_name_list = []
    email_list = []
    availability_list = []
    # password_list = []

    for item in items:
        first_name_list.append(item.employee_first_name)
        last_name_list.append(item.employee_last_name)
        email_list.append(item.employee_email)
        availability_list.append(item.employee_availability)
        # password_list.append(item.password)

    return (
        first_name_list,
        last_name_list,
        email_list,
        availability_list,
        # password_list
    )


@app.route("/")
def index():
    print(current_user)
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for("main"))
    return flask.render_template("login.html")


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(task_id):
    return Staff.query.get(task_id)


def email_format(email):
    email = email.lower()
    print(email)
    return email


def logger(user):
    login_user(user)
    print(user)
    return user


@app.route("/login", methods=["POST"])
def login_post():
    employee_email = flask.request.form["email"]
    employee_email = email_format(employee_email)
    user = Staff.query.filter_by(employee_email=employee_email).first()

    error = None
    if user:
        logger(user)
        return flask.redirect(flask.url_for("index"))

    else:
        return render_template(
            "login.html",
            error="Invail login. Please sign up!",
        )


def already_User(first_name_list, last_name_list, email_list, availability_list):
    alreadyUser = False
    input_firstName = flask.request.form.get("firstName")
    input_lastName = flask.request.form.get("lastName")
    input_email = flask.request.form.get("email")
    input_availability = flask.request.form.get("availability")
    # input_password = flask.request.form.get("password")

    for firstName in first_name_list:
        if firstName == input_firstName:
            alreadyUser = True
    for lastName in last_name_list:
        if lastName == input_lastName:
            alreadyUser = True
    for email in email_list:
        if email == input_email:
            alreadyUser = True
    for availability in availability_list:
        if availability == input_availability:
            alreadyUser = True
    # for password in password_list:
    #     if (password == input_password):
    #         alreadyUser = True
    return (input_firstName, input_lastName, input_email, alreadyUser)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        first_name_list, last_name_list, email_list, availability_list = getDB()

        input_firstName, input_lastName, input_email, alreadyUser = already_User(
            first_name_list, last_name_list, email_list, availability_list
        )

        if alreadyUser == False:
            new_employee = Staff(
                employee_first_name=input_firstName,
                employee_last_name=input_lastName,
                employee_email=input_email,
                employee_availability="test",
            )
            db.session.add(new_employee)
            db.session.commit()
            return flask.redirect("/")

    return flask.render_template("signup.html")


def user_preference():
    curr_user = Staff.query.filter_by(
        employee_email=current_user.employee_email
    ).first()
    name = curr_user.employee_first_name
    return name


@app.route("/main")
@login_required
def main():

    name = user_preference()

    return flask.render_template("staffView.html", name=name)


@app.route("/staffInfo")
def staffInfo():
    # if flask.request.method == 'POST':

    first_name_list, last_name_list, email_list, availability_list = getDB()
    length = len(first_name_list)

    return flask.render_template(
        "staffInfo.html",
        first_name_list=first_name_list,
        last_name_list=last_name_list,
        email_list=email_list,
        length=length,
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect("/")


@app.route("/pendingStaff")
def pendingStaff():
    return flask.render_template("pendingStaff.html")


@app.route("/shiftChange")
def shiftChange():
    return flask.render_template("shiftChange.html")


if __name__ == "__main__":
    app.run(debug=True)
