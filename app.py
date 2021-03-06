import logging
from logging import error
import os
from dotenv import load_dotenv, find_dotenv
import flask
from flask_login import login_user, LoginManager, current_user, UserMixin
import flask_login
from flask_login.utils import login_required, logout_user
from flask.templating import render_template
import datetime

import json

# from pythongrid_app.grid import PythonGrid
# from pythongrid_app.data import PythonGridDbData
# from pythongrid_app.export import PythonGridDbExport
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://jfrudxnfhgiarz:37dbab76396127b98a5e05f2ce6ffa61dc24e9c9f7b9857273f0db644acff864@ec2-34-199-224-49.compute-1.amazonaws.com:5432/d5ciau5h4uuf4i"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = b"os.getenv('APP_SECRET_KEY')"

db = SQLAlchemy(app)


class Staff(db.Model, UserMixin):
    task_id = db.Column(db.Integer, primary_key=True)
    employee_first_name = db.Column(db.String(120), nullable=False)
    employee_last_name = db.Column(db.String(120), nullable=False)
    employee_email = db.Column(db.String(180), nullable=False)
    employee_availability = db.Column(db.String(65535), nullable=True)
    employee_password = db.Column(db.String(180), nullable=False)

    def get_id(self):
        return self.task_id


class Manager(db.Model, UserMixin):
    task_id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.String(120), nullable=False)
    manager_email = db.Column(db.String(120), nullable=False)

    def get_id(self):
        return self.task_id


db.create_all()


#### Managers are not allowed to signup , must be manually added to manager database
new_manager_john = Manager(
    manager_name="John Martin", manager_email="jmartin191@gsu.edu"
)
new_manager = Manager(
    manager_name="Manager_Login", manager_email="barhop.4350@gmail.com"
)
db.session.add(new_manager, new_manager_john)
db.session.commit()

# function to get datas stored in database
def getDB():

    items = Staff.query.all()

    first_name_list = []
    last_name_list = []
    email_list = []
    availability_list = []
    password_list = []

    for item in items:
        first_name_list.append(item.employee_first_name)
        last_name_list.append(item.employee_last_name)
        email_list.append(item.employee_email)
        availability_list.append(item.employee_availability)
        password_list.append(item.employee_password)

    return (
        first_name_list,
        last_name_list,
        email_list,
        availability_list,
        password_list,
    )

@app.route("/", methods=["GET", "POST"])
def index():

    if current_user.is_authenticated:
        print("\n\nSomething is VERY wrong\n\n\n")
        return flask.redirect(flask.url_for("main"))
    print("Something is very right?")
    return flask.render_template("login.html")


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(task_id):
    return Staff.query.get(task_id)

def email_format(email):
    email = email.lower()
    return email

def logger(user):
    login_user(user)
    return user

def displayMessage(type):
    if type == "No email":
        error = "No email entered , please sign in!"
    elif type == "Invalid Login":
        error = "Invalid login. Please sign up!"
    elif type == "Signup":
        error = "Error. Please try again!"
    else:
        error = "Unknown error!"
    return error

# function for login
@app.route("/login", methods=["POST"])
def login_post():
    employee_email = flask.request.form["email"]
    employee_email = email_format(employee_email)
    employee_password = flask.request.form["password"]

    # See what user is,
    user = Staff.query.filter_by(employee_email=employee_email).first()

    management = Manager.query.filter_by(manager_email=employee_email).first()
    error = None

    if user:
        user_password = user.employee_password
        logger(user)
        if user_password == employee_password:
            return flask.redirect(flask.url_for("index"))
        else:
            return render_template(
                "login.html",
                error="Invalid login or password. Please sign up!",
            )

    if management:
        # User session will be started for management
        logger(management)
        name = management.manager_name
        return flask.redirect(flask.url_for("managerView"))

    if employee_email == "":
        return render_template(
            "login.html",
            error=displayMessage("No email"),
        )
    else:
        return render_template(
            "login.html",
            error=displayMessage("Invalid Login"),
        )


def already_User(first_name_list, last_name_list, email_list, password_list):
    alreadyUser = False
    input_firstName = flask.request.form.get("firstName")
    input_lastName = flask.request.form.get("lastName")
    input_email = flask.request.form.get("email")
    input_password = flask.request.form.get("password")

    for email in email_list:
        if email == input_email:
            alreadyUser = True
    return (input_firstName, input_lastName, input_email, input_password, alreadyUser)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        (
            first_name_list,
            last_name_list,
            email_list,
            password_list,
            availability_list,
        ) = getDB()

        (
            input_firstName,
            input_lastName,
            input_email,
            input_password,
            alreadyUser,
        ) = already_User(first_name_list, last_name_list, email_list, password_list)

        input_availability_start_time = flask.request.form.getlist(
            "availability-start-time"
        )
        input_availability_end_time = flask.request.form.getlist(
            "availability-end-time"
        )
        input_availability_date = flask.request.form.getlist("availability-date")
        # Add validation that all 3 above are of equal length
        availabilities = []
        for i in range(len(input_availability_date)):
            avail_string = f"{input_availability_date[i]}_{input_availability_start_time[i]}_{input_availability_end_time[i]}"
            availabilities.append(avail_string)
        if alreadyUser == False:
            new_employee = Staff(
                employee_first_name=input_firstName,
                employee_last_name=input_lastName,
                employee_email=input_email,
                employee_password=input_password,
                employee_availability="#".join(availabilities),
            )
            db.session.add(new_employee)
            db.session.commit()
            return flask.redirect("/")
        else:
            return flask.render_template("signup.html", error = displayMessage("Signup"))
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

    curr_user = Staff.query.filter_by(
        employee_email=current_user.employee_email
    ).first()

    all_users = Staff.query.all()
    name = user_preference()

    data = []
    availability = curr_user.employee_availability
    availability_list = availability.split("#")
    for avail in availability_list:
        split_date = avail.split("_")
        start = f"{split_date[0]}T{split_date[1]}"
        end = f"{split_date[0]}T{split_date[2]}"
        data.append({"start": start, "end": end, "allDay": False})

    for i in range(len(availability_list)):
        split_list = availability_list[i].split("_")
        availability_list[
            i
        ] = f"{split_list[0]}: from {split_list[1]} to {split_list[2]}"
    if curr_user.employee_email == "a10@a":
        return flask.render_template("managerView.html")

    return flask.render_template(
        "staffView.html",
        name=name,
        availability=availability_list,
        availability_times=data,
    )


@app.route("/changeAvailability", methods=["GET", "POST"])
def changeAvailability():
    if flask.request.method == "POST":
        curr_user = Staff.query.filter_by(
            employee_email=current_user.employee_email
        ).first()

        input_availability_start_time = flask.request.form.getlist(
            "availability-start-time"
        )
        input_availability_end_time = flask.request.form.getlist(
            "availability-end-time"
        )
        input_availability_date = flask.request.form.getlist("availability-date")
        # Add validation that all 3 above are of equal length
        availabilities = []
        for i in range(len(input_availability_date)):
            avail_string = f"{input_availability_date[i]}_{input_availability_start_time[i]}_{input_availability_end_time[i]}"
            availabilities.append(avail_string)

        curr_user.employee_availability = "#".join(availabilities)
        db.session.commit()

        return flask.redirect("/main")

    return flask.render_template("changeAvailability.html")


@app.route("/managerView")
def managerView():
    all_users = Staff.query.all()
    data = []

    for user in all_users:
        availability_list = user.employee_availability.split("#")
        availability_list = list(
            filter(lambda availability: availability != "__", availability_list)
        )
        for avail in availability_list:
            split_date = avail.split("_")
            start = f"{split_date[0]}T{split_date[1]}"
            end = f"{split_date[0]}T{split_date[2]}"
            data.append(
                {
                    "start": start,
                    "end": end,
                    "allDay": False,
                    "title": f"{user.employee_first_name} {user.employee_last_name}",
                }
            )

    return flask.render_template(
        "managerView.html", name="Manager_Login", availability_times=data
    )

# function to load staffInfo page used with manager user for sprint 2
@app.route("/staffInfo", methods=["GET", "POST"])
def staffInfo():
    if flask.request.method == "POST":
        first_name_list, last_name_list, email_list, availability_list, password_list = getDB()
        chosen_Staff = flask.request.form.get("staffList")

        for email in email_list:
            if chosen_Staff == email:
                deleteStaff = Staff.query.filter_by(employee_email=email).first()
                db.session.delete(deleteStaff)
                db.session.commit()

    first_name_list, last_name_list, email_list, availability_list, password_list = getDB()
    length = len(first_name_list)

    return flask.render_template(
        "staffInfo.html",
        first_name_list=first_name_list,
        last_name_list=last_name_list,
        email_list=email_list,
        length=length,
    )


@app.route("/calendar")
def calendar():
    data = {
        "availability": [
            {
                "start": "2021-12-10T00:00:00",
                "end": "2021-12-10T24:00:00",
                "display": "background",
            }
        ]
    }
    return render_template("calendar.html", data=data)


@app.route("/logout")
def logout():
    print(current_user)
    logout_user()
    return flask.redirect("/")

@app.route("/scheduling")
def scheduling():
    my_date = datetime.date.today()
    first_name_list, last_name_list, email_list, availability_list = getDB()

    year, week_num, day_of_week = my_date.isocalendar()
    return render_template(
        "scheduling.html", week_num=week_num, year=year, first_name_list=first_name_list
    )


@app.route("/shiftChange")
def shiftChange():
    return flask.render_template("shiftChange.html")

# function used for testing, check if email is in the database or not
def checkEmail(input_email):
    first_name_list, last_name_list, email_list, availability_list, password_list = getDB()
    for item in email_list:
        if input_email == item:
            return True
    return False

# function used for testsing, rcheck if the names are in the database or not
def checkNames(input_firstName, input_lastName):
    first_name_list, last_name_list, email_list, availability_list, password_list = getDB()
    statusF = False
    statusN = False
    for name in first_name_list:
        if input_firstName == name:
            statusF = True
    for name in last_name_list:
        if input_lastName == name:
            statusN = True
    if statusF == statusN:
        return True
    return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=True)
