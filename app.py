from flask import Flask, redirect, render_template, url_for, request, Markup
import os
import pymongo
import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import re
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import math

# load env file
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

DB_NAME = "onetworun"

app = Flask(__name__)

TOP_LEVEL_DIR = os.path.abspath(os.curdir)
upload_dir = '/static/uploads/img/'
app.config["UPLOADS_DEFAULT_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_URL"] = upload_dir

images_upload_set = UploadSet('images', IMAGES)
configure_uploads(app, images_upload_set)

categories = ["Marathon","Half Marathon","Sprint", "Short Distance", "Weight Loss", "Everyone"]
difficulty = ["Easy","Intermediate", "Advanced", "Professional"]

@app.route('/')
def home():
    return render_template("index.template.html")

@app.route('/show_programmes', methods=["GET"])
def show_programmes(): 
    search_title = request.args.get('search-by')
    search_category = request.args.getlist('search-category')
    search_difficulty = request.args.getlist('search-difficulty')
    search_criteria = {}

    #pagination for show programmes
    show_per_page = 4
    max_pages = math.ceil(client[DB_NAME].programmes.count() / show_per_page)

    current_page = int(request.args.get('current_page',1))

    #only show first ten
    

    
    if request.method =="GET":
        cursor = client[DB_NAME].programmes.find().sort('date', pymongo.DESCENDING).skip((show_per_page)*(current_page-1)).limit(show_per_page)
        if search_title: 
            search_criteria["title"] = re.compile(r'{}'.format(search_title), re.I)
            
        
        if len(search_category) > 0: 
            search_criteria["category"] = {
                '$all': search_category
            }
            print(search_category)

        if len(search_difficulty) > 0: 
            search_criteria["difficulty"] = {
                '$all': search_difficulty
            }

        projection={'title',"duration","difficulty","category", "image_url", "date_of_post", "author"}

        cursor = client[DB_NAME].programmes.find(search_criteria, projection).skip((show_per_page)*(current_page-1)).limit(show_per_page)

    return render_template('show_programmes.template.html', results = cursor, categories = categories, difficulties = difficulty, max_pages = max_pages)

@app.route('/create_programmes', methods=["GET","POST"])
def create_programmes():
    if request.method=="GET":
        return render_template('create_programmes.template.html')
    
    if request.method=="POST":
        client[DB_NAME].programmes.insert_one({
            "title": request.form.get('programme_title'),
            "image_url": request.form.get("image"),
            "difficulty": request.form.get('programme_difficulty'),
            "category": request.form.get('programme_category'),
            "date": datetime.datetime.strptime(request.form.get('programme_date'), "%Y-%m-%d"),
            "time": datetime.datetime.strptime(request.form.get("programme_time"), '%H:%M'),
            "description": request.form.get("programme_description"),
            "duration": request.form.get('programme_duration'),
            "location": request.form.get("programme_location"),
            "author": request.form.get("programme_author"), 
            "date_of_post": datetime.datetime.now()
        })
    return redirect(url_for("show_programmes"))

@app.route('/programme_details/<programme_id>' ,methods=["GET","POST"])
def programme_detail(programme_id):
    programme = client[DB_NAME].programmes.find_one({
        "_id": ObjectId(programme_id)
    })

    if request.method == "GET": 
        return render_template('programme_details.template.html', programme = programme)

    if request.method == "POST": 
        client[DB_NAME].programmes.update_one({ 
            "_id": ObjectId(programme_id)
        }, {
            '$push': {
                'reviews':{
                    '_id': ObjectId(),
                    'programme_id': ObjectId(programme_id),
                    'name': request.form.get('reviewer_name'),
                    'review': request.form.get('review'),
                    'date_review': datetime.datetime.now()
                }
            }
        })
        return redirect(url_for("programme_detail", programme_id = programme_id))

    return render_template('programme_details.template.html', programme = programme)



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
                "image_url": request.form.get("image"),
                "difficulty": request.form.get('programme_difficulty'),
                "category": request.form.get('programme_category'),
                "date": datetime.datetime.strptime(request.form.get('programme_date'), "%Y-%m-%d"),
                "time": datetime.datetime.strptime(request.form.get("programme_time"), '%H:%M'),
                "description": request.form.get("programme_description"),
                "duration": request.form.get('programme_duration'),
                "location": request.form.get("programme_location")
            }
        })
        return redirect(url_for("show_programmes"))




if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )