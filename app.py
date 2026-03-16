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

    # allow any login as long as fields are filled
    if username and password:
        session['user'] = username
        return redirect("/dashboard")
    else:
        return "Please enter username and password"


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("dashboard.html", tasks=tasks, user=session['user'])
    else:
        return redirect("/")


@app.route('/add', methods=['POST'])
def add():
    if 'user' in session:
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect("/dashboard")
    else:
        return redirect("/")


@app.route('/delete/<int:id>')
def delete(id):
    if 'user' in session:
        if 0 <= id < len(tasks):
            tasks.pop(id)
        return redirect("/dashboard")
    else:
        return redirect("/")


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)