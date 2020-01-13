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


@app.route('/edit_entry/<entry_id>')
def edit_entry(entry_id):
    the_entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    return render_template('editentry.html', entry=the_entry)


@app.route('/update_entry/<entry_id>', methods=['POST'])
def update_entry(entry_id):
    entries = mongo.db.entries
    entries.update({'_id': ObjectId(entry_id)},
            {
                'name': request.form.get('name'),
                'description': request.form.get('description'),
                'upvotes': request.form.get('upvotes')
            })
    return redirect(url_for('index'))


@app.route('/delete_entry/<entry_id>')
def delete_entry(entry_id):
    mongo.db.entries.remove({'_id': ObjectId(entry_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
