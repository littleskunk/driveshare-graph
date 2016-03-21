import settings
from pymongo import MongoClient
from pycoin.encoding import a2b_hashed_base58
from binascii import hexlify

connection = MongoClient('localhost', 27017)
collection = connection[settings.DBS_NAME][settings.FARMERS_COLLECTION]

for farmer in collection.find().distinct('farmers.btc_addr'):
    nodeid = hexlify(a2b_hashed_base58(farmer)[1:]).decode("utf-8")
    print(nodeid)
    collection.update_many({'farmers.btc_addr': farmer}, 
                           {'$set': {'farmers.$.nodeid': nodeid}, 
                            '$unset': {'farmers.$.btc_addr': ''}}) 

connection.close()
