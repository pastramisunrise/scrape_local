import pymongo

class Business():

    def __init__(self, info = {}, table = ""):
        self.info = info
        self.table = table
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["bus_db"]
        self.col = self.db[self.table]

    def find_bus(self):
        query = {"cartodb_id" : self.info["cartodb_id"]}
        docs = self.col.find(query).count()
        return docs > 0

    def add_record(self):
        x = self.col.insert_one(self.info)
        return x.inserted_id