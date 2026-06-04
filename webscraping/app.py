from flask import Flask, render_template, request
import json
app = Flask(__name__)

with open("books.json") as f:
    booklist = json.load(f)

@app.route("/")
def home():
    return render_template("home.html", books=booklist)


@app.route("/five")
def fivebook():
    fivebooks = [ book for book in booklist if book["rating"]=="Five"]
    return render_template("homefive.html", books = fivebooks)

@app.route("/four")
def fourbook():
    fourbooks = [ book for book in booklist if book["rating"]=="Four"]
    return render_template("homefour.html", books = fourbooks)

@app.route("/three")
def threebook():
    threebooks = [ book for book in booklist if book["rating"]=="Three"]
    return render_template("homethree.html", books = threebooks)

@app.route("/two")
def twobook():
    twobooks = [ book for book in booklist if book["rating"]=="Two"]
    return render_template("hometwo.html", books = twobooks)

@app.route("/one")
def onebook():
    onebooks = [book for book in booklist if book["rating"=='One']]
    return render_template("homeone.html", books = onebooks)


@app.route("/search")
def search():
    query = request.args.get("q","")
    results = [book for book in booklist if query.lower() in book["title"].lower()]
    return render_template("search.html",books = results , query = query)

app.run(debug = True)