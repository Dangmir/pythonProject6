import requests
import pymongo
import datetime
import time
client = pymongo.MongoClient("mongodb+srv://lexa324sa:nuBAapK0ugNy2Rfg@cluster0.jb34r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["cursbtc"]
dbs = client['course']

def insert_one():
    a = get_cource()
    day = datetime.datetime.now().isoformat('|','minutes')
    btc = {
        "date":day,
        "course":a
    }
    dbs.course.insert_one(btc)
    db.cursbtc.insert_one(btc)

def get_cource():

    requesta = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    data = requesta.json()['USD']
    return data

insert_one()
