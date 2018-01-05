from pymongo import MongoClient
import pymongo
import re

'''
- `type`: CS for common stock, future for future

- `code`: 
'''


class MongoHelper(object):
    host = "localhost"
    port = 27017

    stock_min_db = "A_stock_min"
    stock_min_collection = "A_stock_min"

    future_client = MongoClient("localhost", 27017)
    future_db = future_client['VnTrader_1Min_Db']

    def __init__(self, host="localhost", port=27017):
        self.host = host
        self.port = port

        self.client = MongoClient(self.host, self.port)
        self.stock_db = self.client[self.stock_min_db]

    def latest_date(self, code, type="CS"):
        if type == "CS":
            cursor = self.stock_db[code].find().sort(
                [("dt", pymongo.DESCENDING)]).limit(1)
            try:
                date = cursor.next()['dt']
            except Exception as e:
                date = None
            return date
        elif type == "future":
            collection = self.future_db[code]
            cursor = collection.find({}, {"date": 1, "_id": 0}).sort([("datetime", pymongo.DESCENDING)]).limit(1)
            try:
                date = cursor.next()['date']
            except Exception as e:
                date = None
            return date

    def get_order_book_id(self, code):
        if code[-2:] == "SH":
            return code[:-2] + "XSHG"
        else:
            return code[:-2] + "XSHE"

    def get_stock_code(self, code):
        if code[-4:] == "XSHG":
            return code[:-4] + "SH"
        else:
            return code[:-4] + "SZ"

    def insert(self, code, data, type="CS"):
        if type == "CS":
            self.stock_db[code].insert(data)
        elif type == "future":
            self.future_db[code].insert(data)
