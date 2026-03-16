from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "agileproject"

tasks = []

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == "student" and password == "1234":
        session['user'] = username
        return redirect("/dashboard")
    else:
        return "Invalid Login"

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("dashboard.html", tasks=tasks)
    else:
        return redirect("/")

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect("/dashboard")

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)