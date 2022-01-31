import json
import os
import pymongo
from bson.objectid import ObjectId


class User:
    def __init__(self, discord_id: int):
        self.id = discord_id
        client = pymongo.MongoClient("localhost", 27017)
        self.collection = client["stalker_rp"]["users"]
        self.data = self.collection.find_one({"id": self.id})
        self.is_reg = bool(self.data)

    def get_data(self):
        return self.collection.find_one({"id": self.id})

    def update(self, key, value):
        self.collection.update_one({"id": self.id}, {'$set': {key: value}})

    def add_to_inventory(self, item):
        self.collection.update_one({"id": self.id}, {'$push': {"inventory": item}})

    def remove_from_inventory(self, item_id):
        self.collection.update_one({"id": self.id}, {'$pull': {"inventory": {"_id": ObjectId(item_id)}}})

    def __getitem__(self, item):
        return self.get_data()[item]


class UserJson:
    def __init__(self, user_id: int):
        self.id = user_id
        self.json = json.load(open(str(os.getcwd()) + f"\\server\\profiles\\{user_id}.json"))

    def __getitem__(self, item):
        return self.json[item]

    def dump(self):
        json.dump(self.json, open(str(os.getcwd()) + f"\\server\\profiles\\{self.id}.json", "w"))
