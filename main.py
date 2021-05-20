import pymongo
import datetime
import nicehash
import time
client = pymongo.MongoClient("mongodb+srv://lexa324sa:nuBAapK0ugNy2Rfg@cluster0.jb34r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["income"]
dbs = client["balance"]
def getBal():
    host = 'https://api2.nicehash.com'
    organisation_id = 'd1acfcc9-7cf2-4022-9991-b571bac3f0c5'
    key = 'dce48174-65cd-4764-8950-00d8308d6e41'
    secret = 'fe1379f8-c08e-4030-83f0-387c65840ad6f1e6576a-d2f0-4c9a-9da0-bdf2ea22dd79'

    private_api = nicehash.NiceHashPrivateApi(host, organisation_id, key, secret)

    my_accounts = private_api.get_accounts_for_currency("BTC")
    my_rig = private_api.get_mining_rigs()
    print(my_rig.keys())
    a = my_rig.get("miningRigs")
    b = a[0]['devices']
    return my_accounts['totalBalance']
def getBalance():
    host = 'https://api2.nicehash.com'
    organisation_id = 'd1acfcc9-7cf2-4022-9991-b571bac3f0c5'
    key = 'dce48174-65cd-4764-8950-00d8308d6e41'
    secret = 'fe1379f8-c08e-4030-83f0-387c65840ad6f1e6576a-d2f0-4c9a-9da0-bdf2ea22dd79'

    private_api = nicehash.NiceHashPrivateApi(host, organisation_id, key, secret)

    my_accounts = private_api.get_accounts_for_currency("BTC")
    my_rig = private_api.get_mining_rigs()
    a = my_rig.get("miningRigs")
    b = a[0]['devices']
    prof = my_rig['totalProfitability']
    return prof
def input_income():
    date = {
        "date":datetime.datetime.now(),
        "income":getBalance()
    }
    db.income.insert_one(date)
def input_balance():
    date = {
        "date":datetime.datetime.now(),
        "balance":getBal()
    }
    dbs.balance.insert_one(date)
while True:
    input_income()
    input_balance()
    time.sleep(30)