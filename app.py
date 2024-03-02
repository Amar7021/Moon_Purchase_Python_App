from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri)
db = client.moonland_DB

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/moon", methods=["POST"])
def moon_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

    db.orders.insert_one(doc)

    return jsonify({'msg': 'complete!'})

@app.route("/moon", methods=["GET"])
def moon_get():
    orders_list = list(db.orders.find({},{'_id':False}))
    print(orders_list)
    return jsonify({'orders':orders_list})
    