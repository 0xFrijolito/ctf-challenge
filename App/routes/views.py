from App import app
from App.helpers import auth

from flask import render_template, make_response, redirect, url_for


@app.route("/", methods=["GET"])
def login ():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register ():
    return render_template("register.html")

@app.route("/dashboard", methods=["GET"])
@auth.is_login
def dashboard (user):
    flag = None
    if user.coins > 1337:
        flag = open("flag.txt", "r").read()
    return render_template("dashboard.html", flag=flag)

@app.route("/logout")
def logout ():
    resp = make_response(redirect(url_for("login")))
    resp.set_cookie('session', '', expires=0)
    return resp