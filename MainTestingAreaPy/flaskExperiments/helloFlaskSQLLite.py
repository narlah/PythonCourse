import os
import smtplib
import sqlite3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db_not_prepared = True


@app.route("/")  # form to list ppl and register
def index():
    return render_template("index.html")


@app.route("/registrants")  # view
def registrants():
    global db_not_prepared
    if db_not_prepared:
        prepareDB()
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    students = []
    for row in c.execute('''SELECT * FROM students ORDER BY name'''):
        students.append(", ".join(row))
    conn.close()
    return render_template("registrants.html", students=students)


@app.route("/register", methods=["POST"])  # business logic to save things and show list
def register():
    global db_not_prepared
    if db_not_prepared:
        prepareDB()
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    email = request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students VALUES(?,?,?)''',
              (request.form["name"], request.form["dorm"], request.form["email"]))
    conn.commit()
    conn.close()
    return redirect("registrants")


def prepareDB():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    print("in create table students")
    c.execute('''CREATE table IF NOT EXISTS students (name text, email text, dorm text)''')
    conn.commit()
    conn.close()
    global db_not_prepared
    db_not_prepared = False


def send_email(email):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    password = os.getenv("EMAIL_PASS")
    server.login(email, password)
    server.sendmail(email, email, "You are registered")
