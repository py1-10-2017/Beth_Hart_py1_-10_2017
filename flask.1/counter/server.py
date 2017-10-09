from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)
app.secret_key = "mikaylamommy"

@app.route('/')
def counter():
    return render_template('index.html')

@app.route("/add", methods=["POST"])
def count():
     session['counter'] += 2
     return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect("/")
    
app.run(host="0.0.0.0", port=int("8080"), debug=True)