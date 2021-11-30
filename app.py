import logging
from logging import error
import os
from dotenv import load_dotenv, find_dotenv
import flask
from flask_login import login_user, LoginManager, current_user, UserMixin
import flask_login
from flask_login.utils import login_required, logout_user
from flask.templating import render_template

# from pythongrid_app.grid import PythonGrid
# from pythongrid_app.data import PythonGridDbData
# from pythongrid_app.export import PythonGridDbExport
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://sggmedeucfzqbo:817307a94016431c320ff1403aa1b2f95c7bd71da6abc999ed157e826910c852@ec2-54-157-16-125.compute-1.amazonaws.com:5432/d61tam9105a164"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = b"os.getenv('APP_SECRET_KEY')"

db = SQLAlchemy(app)


class Staff(db.Model, UserMixin):
    task_id = db.Column(db.Integer, primary_key=True)
    employee_first_name = db.Column(db.String(120), nullable=False)
    employee_last_name = db.Column(db.String(120), nullable=False)
    employee_email = db.Column(db.String(180), nullable=False)
    employee_availability = db.Column(db.String(180), nullable=True)

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

    for item in items:
        first_name_list.append(item.employee_first_name)
        last_name_list.append(item.employee_last_name)
        email_list.append(item.employee_email)
        availability_list.append(item.employee_availability)

    return (
        first_name_list,
        last_name_list,
        email_list,
        availability_list,
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
    print(email)
    return email


def logger(user):
    login_user(user)
    print(user)
    return user


# function for login


@app.route("/login", methods=["POST"])
def login_post():
    employee_email = flask.request.form["email"]
    employee_email = email_format(employee_email)
    user = Staff.query.filter_by(employee_email=employee_email).first()
    management = Manager.query.filter_by(manager_email=employee_email).first()
    error = None

    if user:
        logger(user)
        return flask.redirect(flask.url_for("index"))

    if management:
        # User session will be started for management
        logger(management)
        name = management.manager_name
        return flask.render_template("managerView.html", name=name)

    if employee_email == "":
        return render_template(
            "login.html",
            error="No email entered , please sign in!",
        )
    else:
        return render_template(
            "login.html",
            error="Invalid login. Please sign up!",
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

    # first_name_list, last_name_list, email_list, availability_list = getDB()
    # availability = []
    # curr_user = Staff.query.filter_by(
    #     employee_email=current_user.employee_email
    # ).first()

    # name = curr_user.employee_first_name
    # list = name.employee_availability
    # list = str(list)[1:-1]
    # list = list.replacwe('"', "")
    # availability = list.split(",")

    # length = len(first_name_list)

    # return flask.render_template(
    #    "staffView.html",
    # name=name,
    # length=length,
    # first_name_list=first_name_list,
    # last_name_list=last_name_list,
    # availability=availability,
    # )

    name = user_preference()
    curr_user = Staff.query.filter_by(
        employee_email=current_user.employee_email
    ).first()

    list = curr_user.employee_availability
    list = str(list)[1:-1]
    list = list.replace('"', "")
    availability = list.split(",")

    return flask.render_template(
        "staffView.html",
        name=name,
        availability=availability,
    )


@app.route("/changeAvailability", methods=["GET", "POST"])
def changeAvailability():
    if flask.request.method == "POST":
        curr_user = Staff.query.filter_by(
            employee_email=current_user.employee_email
        ).first()

        input_availability = flask.request.form.getlist("availability")
        print(input_availability)
        curr_user.employee_availability = input_availability
        print(curr_user.employee_availability)
        db.session.commit()

        return flask.redirect("/main")

    return flask.render_template("changeAvailability.html")


# function used for testing, check if email is in the database or not
def checkEmail(input_email):
    first_name_list, last_name_list, email_list, availability_list = getDB()

    for item in email_list:
        print(item)
        if input_email == item:
            return True
    return False


# function used for testsing, returns first name of employee based on email
def checkName(input_email):
    user = Staff.query.filter_by(employee_email=input_email).first()
    first_name = user.employee_first_name
    return first_name


# function used for testing, return the availability for the chosen user
def returnAvailability(input_email):

    # <<<<<<< Rice_branch
    # curr_user = Staff.query.filter_by(input_email=current_user.employee_email).first()

    # availability = curr_user.employee_availability

    # return availability

    # =======
    user = Staff.query.filter_by(employee_email=input_email).first()
    availability = user.employee_availability

    return availability


# function to load staffInfo page used with manager user for sprint 2
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


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/logout")
def logout():
    print(current_user)
    logout_user()
    return flask.redirect("/")


@app.route("/pendingStaff")
def pendingStaff():
    return flask.render_template("pendingStaff.html")


@app.route("/scheduling")
def scheduling():
    grid = PythonGrid('"SELECT * FROM Staff", "employee_name"')
    return render_template("scheduling.html", title="GRID", grid=grid)


@app.route("/shiftChange")
def shiftChange():
    return flask.render_template("shiftChange.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=True)
