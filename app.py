<<<<<<< HEAD
from logging import error
import os
import flask
from flask_login import login_user, LoginManager, current_user, UserMixin
from flask_login.utils import login_required
from flask.templating import render_template

=======
import os
import flask
from flask_login import login_user
>>>>>>> 9a4cfd6969bbdb6f634844535f66ca2f7ddfd65b
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://luluzeugoxqaba:f082d0f1f1f01321bfe2e94fd176374166edda647252c2e795b5a9a189970816@ec2-107-23-135-132.compute-1.amazonaws.com:5432/d3v8dftmvr631l"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


<<<<<<< HEAD
class Staff(db.Model, UserMixin):
=======
class Staff(db.Model):
>>>>>>> 9a4cfd6969bbdb6f634844535f66ca2f7ddfd65b
    task_id = db.Column(db.Integer, primary_key=True)
    employee_first_name = db.Column(db.String(120), nullable=False)
    employee_last_name = db.Column(db.String(120), nullable=False)
    employee_email = db.Column(db.String(180), nullable=False)
    employee_availability = db.Column(db.String(180), nullable=True)
<<<<<<< HEAD
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
=======
    password = db.Column(db.String(180), nullable=True)


db.create_all()
>>>>>>> 9a4cfd6969bbdb6f634844535f66ca2f7ddfd65b


@app.route("/")
def index():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for("/main"))
    return flask.render_template("login.html")


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(employee_email):
    return Staff.query.get(employee_email)


@app.route("/login", methods=["POST"])
def login_post():
    employee_email = flask.request.form["email"]
    user = Staff.query.filter_by(employee_email=employee_email).first()
    error = None

    if user:
        login_user(user)
        return flask.redirect(flask.url_for("index"))

    else:
        return render_template(
            "login.html",
            error="Invail login. Please sign up!",
        )


# Anna's Login -------------------------------------------------------------------
# @app.route("/login", methods = ["POST"])
# def login():

#     input_email = flask.request.form.get("email")

#     first_name_list, last_name_list, email_list, availability_list = getDB()

#     for email in email_list:
#         if email == input_email:
#             # for password in password_list:
#             #     if password == input_password:
#             return flask.redirect("/main")
#     return flask.redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        alreadyUser = False

        input_firstName = flask.request.form.get("firstName")
        input_lastName = flask.request.form.get("lastName")
        input_email = flask.request.form.get("email")
        input_availability = flask.request.form.get("availability")
        # input_password = flask.request.form.get("password")

        first_name_list, last_name_list, email_list, availability_list = getDB()

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


@app.route("/main")
@login_required
def main():

<<<<<<< HEAD
    # new_employee = Staff(
    #     employee_first_name="test_rice",
    #     employee_last_name="test_maxwell",
    #     employee_email="test_group@project.com",
    #     employee_availability="test never",
    # )
    # db.session.add(new_employee)
    # db.session.commit()
    return flask.render_template("staffView.html")
    # return flask.render_template("managerView.html")


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


@app.route("/pendingStaff")
def pendingStaff():
    return flask.render_template("pendingStaff.html")


@app.route("/shiftChange")
def shiftChange():
    return flask.render_template("shiftChange.html")
=======
    new_employee = Staff(
        employee_first_name="test_rice",
        employee_last_name="test_maxwell",
        employee_email="test_group@project.com",
        employee_availability="test never",
    )
    db.session.add(new_employee)
    db.session.commit()
    return flask.render_template("index.html")
>>>>>>> 9a4cfd6969bbdb6f634844535f66ca2f7ddfd65b


if __name__ == "__main__":
    app.run(debug=True)
