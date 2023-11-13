from flask import Flask
from flask import request
from flask import render_template
midterm = Flask(__name__)
@midterm.route("/")
def main():
    return render_template("login.html")

@midterm.route("/registration.html")
def registration():
    return render_template("registration.html")

#for redirecting to login page from registration page
@midterm.route("/login.html") 
def login():
    return render_template("login.html")

if __name__ == "__main__":
    midterm.run(host="0.0.0.0", port=5000)
