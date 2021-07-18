import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.eniron.get('MONGODB_URI'))
    app.db = client.data_collection_db

    @app.route('/',methods=['GET','POST'])
    def home():
        if (request.method == 'POST'):
            content = request.form.get('content')
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert({"content":content,"date":formatted_date})
        a = render_template("first_page.html")
        a = a+render_template("atable.html",entries=app.db.entries.find({}))
        return a 
    return app
