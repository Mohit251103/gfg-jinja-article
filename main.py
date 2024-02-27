from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",user="Mohit Negi")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html",user_list=["Mohit","GFG"])

@app.route("/fourth")
def fourth():
    return render_template("child_template.html",user="Mohit Negi")

app.run()