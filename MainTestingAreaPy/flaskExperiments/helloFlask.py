import os
import smtplib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []


@app.route("/")  # form to list ppl and register
def index():
    return render_template("index.html")


@app.route("/registrants")  # view
def registrants():
    return render_template("registrants.html", students=students)


@app.route("/register", methods=["POST"])  # business logic to save things and show list
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    email = request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    password = os.getenv("EMAIL_PASS")
    server.login(email, password)
    server.sendmail(email, email, "You are registered")
    students.append(f"{name} from {dorm} with {email}")
    print(students)
    return redirect("registrants")
