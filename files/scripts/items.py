import json
import os
import pymongo
from bson.objectid import ObjectId


class Item:
    def __init__(self, _id: ObjectId):
        self._id = _id
        client = pymongo.MongoClient("localhost", 27017)
        self.collection = client["stalker_rp"]["items"]
        self.data = self.collection.find_one({"_id": self._id})   

    def get_data(self):
        self.data = self.collection.find_one({"_id": self._id})
        return self.data

    def update(self, key, value):
        self.collection.update_one({"_id": self._id}, {'$set': {key: value}})

    def add_to_inventory(self, item):
        self.collection.update_one({"_id": self._id}, {'$push': {"inventory": item}})
        
    def __getitem__(self, item):
        return self.get_data()[item]
    
item_mask = {
        "tpl": "",
        "modules": {},
        "parameters":{},
  }
    
