from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hi():
    name = request.args.get("name", "World")
    return render_template("index.html", name=name)

