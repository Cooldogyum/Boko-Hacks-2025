from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models.user import User

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user"] = user.username
            flash("Login successful!", "success")
            return redirect(url_for("hub.hub"))
        else:
            flash("Invalid username or password.", "error")

    return render_template("login.html")


@login_bp.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("_flashes", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login.login"))
