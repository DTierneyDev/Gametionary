import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "gametionary"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", entries=mongo.db.entries.find())


@app.route('/add_entry')
def add_entry():
    return render_template("addentry.html")


@app.route('/insert_entry', methods=['POST'])
def insert_entry():
    entries = mongo.db.entries
    entries.insert_one(request.form.to_dict())
    return redirect(url_for('add_entry'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
