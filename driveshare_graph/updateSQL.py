import uptime
import storage
import settings
import time
import pymongo
from pymongo import MongoClient
import sqlite3

while True:
    conn = sqlite3.connect(settings.DB)
    cursor = conn.cursor()
    connection = MongoClient('localhost', 27017)
    collection = connection[settings.DBS_NAME][settings.FARMERS_COLLECTION]
    uptime.update_farmers_table(conn, cursor, collection)
    collection = connection[settings.DBS_NAME][settings.STORAGE_COLLECTION]
    storage.update_stats_table(conn, cursor, collection)
    cursor.close()
    conn.close()
    connection.close()
    time.sleep(30)
