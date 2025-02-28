import os

from dotenv import load_dotenv
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models.user import User
from utils.captcha import verify_hcaptcha

load_dotenv()

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        captcha_response = request.form.get("h-captcha-response")

        if not verify_hcaptcha(captcha_response, request.remote_addr):
            flash("Invalid CAPTCHA. Please try again.", "error")
            return redirect(url_for("register.register"))

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user"] = user.username
            flash("Login successful!", "success")
            return redirect(url_for("hub.hub"))
        else:
            flash("Invalid username or password.", "error")

    return render_template(
        "login.html", HCAPTCHA_SITE_KEY=os.environ.get("HCAPTCHA_SITE_KEY")
    )


@login_bp.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("_flashes", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login.login"))
