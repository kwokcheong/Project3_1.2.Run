from flask import Flask, redirect, render_template, url_for, request, Markup
import os
import pymongo
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv

# load env file
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

DB_NAME = "onetworun"

app = Flask(__name__)


@app.route('/')
def helloworld():
    return render_template("index.template.html")

@app.route('/show_programmes', methods=["GET"])
def show_programmes(): 
    all_programmes = client[DB_NAME].programmes.find()
    return render_template('show_programmes.template.html', results = all_programmes)

@app.route('/create_programmes', methods=["GET","POST"])
def create_programmes():
    if request.method=="GET":
        return render_template('create_programmes.template.html')
    
    if request.method=="POST":
        client[DB_NAME].programmes.insert_one({
            "title": request.form.get('programme_title'),
            "duration": request.form.get('programme_duration'),
            "distance": request.form.get('programme_distance'),
            "description": request.form.get("programme_description")
        })
    return redirect(url_for("show_programmes"))

@app.route("/delete_programmes/<programme_id>")
def delete_programme(programme_id): 
    client[DB_NAME].programmes.remove({
        "_id": ObjectId(programme_id)
    })
    return redirect(url_for('show_programmes'))

@app.route('/edit_programme/<programme_id>', methods=["GET", "POST"])
def edit_programme(programme_id):

    programme = client[DB_NAME].programmes.find_one({
        "_id": ObjectId(programme_id)
    })

    if request.method == "GET": 
        return render_template('edit_programme.template.html', programme = programme)
    if request.method == "POST":
        client[DB_NAME].programmes.update_one({
            "_id": ObjectId(programme_id)
        }, 
        {
            "$set": {
                "title": request.form.get('programme_title'),
                "duration": request.form.get('programme_duration'),
                "distance": request.form.get('programme_distance'),
                "description": request.form.get("programme_description")
            }
        })
        return redirect(url_for("show_programmes"))

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )