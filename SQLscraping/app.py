from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db= SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    done = db.Column(db.Boolean, default = False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks= tasks)

@app.route("/add", methods = ["POST"])
def add():
    title = request.form.get("title")
    new_task = Task(title = title)
    db.session.add(new_task)
    db.session.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

app.run(debug = True)