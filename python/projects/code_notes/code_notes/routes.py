from flask import render_template, url_for, flash, redirect
from code_notes import app
from code_notes.forms import RegistrationForm, LoginForm, WikiPostForm
from code_notes.models import User, Post
import logging


posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/markdown_form", methods=["GET", "POST"])
def markdown_form():
    form = WikiPostForm()
    if form.validate_on_submit():
        flash("Your Note has been Successfully Added!", "success")
        logging.info(f"{form.data}")
    return render_template("markdown_form.html", title="Login", form=form)


@app.route("/wiki", methods=["GET", "POST"])
def wiki():
    return render_template("wiki.html", title="Login")
