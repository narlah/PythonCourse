import os
import smtplib
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
db_not_prepared = True
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    dorm = Column(String(250), nullable=False)


@app.route("/")  # form to list ppl and register
def index():
    return render_template("index.html")


@app.route("/registrants")  # view
def registrants():
    global db_not_prepared
    if db_not_prepared:
        prepareDB()
    session = DBSession()
    students = []
    for student in session.query(Student).all():
        students.append(student.name + " " + student.dorm + " " + student.email)
    return render_template("registrants.html", students=students)


@app.route("/register", methods=["POST"])  # business logic to save things and show list
def register():
    global db_not_prepared
    if db_not_prepared:
        prepareDB()
    session = DBSession()
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    email = request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    newStudent = Student(name=request.form["name"], dorm=request.form["dorm"], email=request.form["email"])
    session.add(newStudent)
    session.commit()
    return redirect("registrants")


def prepareDB():
    engine = create_engine('sqlite:///students2.db')
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    global db_not_prepared
    db_not_prepared = False
    global DBSession
    DBSession = sessionmaker(bind=engine)


def send_email(email):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    password = os.getenv("EMAIL_PASS")
    server.login(email, password)
    server.sendmail(email, email, "You are registered")
