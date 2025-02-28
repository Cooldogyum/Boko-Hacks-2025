import os

from dotenv import load_dotenv
from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models.user import User
from utils.captcha import verify_hcaptcha

load_dotenv()

register_bp = Blueprint("register", __name__)


@register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        captcha_response = request.form.get("h-captcha-response")

        if not verify_hcaptcha(captcha_response, request.remote_addr):
            flash("Invalid CAPTCHA. Please try again.", "error")
            return redirect(url_for("register.register"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose a different one.", "error")
            return redirect(url_for("register.register"))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login.login"))

    return render_template(
        "register.html", HCAPTCHA_SITE_KEY=os.environ.get("HCAPTCHA_SITE_KEY")
    )
