from pymongo import MongoClient

class MongoDB:
    def __init__(self, dbname):
        self._client = MongoClient("localhost", 27017)
        self._db   = self._client[dbname]

    def collection(self, name_collection):
        collection = self._db[name_collection]
        return collection