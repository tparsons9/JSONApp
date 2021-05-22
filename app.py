import os
import json
import pymongo
from flask import Flask
from flask import request

app = Flask(__name__)
client = pymongo.MongoClient('mongodb+srv://Tparsons:Tanner@startingcluster.ktr71.mongodb.net/TheFirstDatabase?retryWrites=true&w=majority')
db = client.TheFirstDatabase
collection = db.InitialAggregation

app.route('/')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

if __name__ == '__main__':
    app.run()