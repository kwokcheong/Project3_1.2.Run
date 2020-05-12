from flask import Flask, redirect, render_template, url_for, request, Markup
import os
import pymongo
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import re

# load env file
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

DB_NAME = "onetworun"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.template.html")

@app.route('/show_programmes', methods=["GET"])
def show_programmes(): 
    search_name = request.args.get('search-by')

    search_criteria = {}
    if search_name is not "": 
        search_criteria["title"] = re.compile(r'{}'.format(search_name), re.I)

    projection={'title'}
    cursor = client[DB_NAME].programmes.find(search_criteria, projection)
    
    return render_template('show_programmes.template.html', results = cursor)

@app.route('/create_programmes', methods=["GET","POST"])
def create_programmes():
    if request.method=="GET":
        return render_template('create_programmes.template.html')
    
    if request.method=="POST":
        client[DB_NAME].programmes.insert_one({
            "title": request.form.get('programme_title'),
            "duration": request.form.get('programme_duration'),
            "difficulty": request.form.get('programme_difficulty'),
            "tag": request.form.get("programme_tags"),
            "category": request.form.get('programme_category'),
            "description": request.form.get("programme_description"),
            "date": datetime.strptime(request.form.get('programme_date'), "%Y-%m-%d"),
            "time": datetime.strptime(request.form.get("programme_time"), '%H:%M'),
            "location": request.form.get("programme_location")
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