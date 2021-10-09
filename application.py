from flask import Flask, render_template, request, redirect

app = Flask(__name__)

COURSES = [
    "Python Core",
    "HTML Core",
    "CSS Core",
    "SQL Core",
]

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html", courses=COURSES)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    course = request.form.get("course")
    if not course:
        return render_template("error.html", message="Missing course")

    REGISTRANTS[name] = course
    return redirect('/registrants')

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)