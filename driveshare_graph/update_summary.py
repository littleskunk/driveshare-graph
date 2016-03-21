import farmer_summary
import settings
import sqlite3
from pymongo import MongoClient
from time import sleep


while(True):
    conn = sqlite3.connect('summary.db')
    cursor = conn.cursor()
    connection = MongoClient('localhost', 27017)
    collection = connection['GroupB']['farmers']
    farmer_summary.update_table(conn, cursor, collection)
    cursor.close()
    conn.close()
    connection.close()
    sleep(86400)
