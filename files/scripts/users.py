import json
import os
import pymongo


class User:
    def __init__(self, user_id: int):
        self.id = user_id
        client = pymongo.MongoClient('localhost', 27017)
        self.db = db = client["stalker_rp"]["users"]
        self.json = db.find_one({"id": user_id})
        self.is_reg = not self.json is None
        print(self.json)

    def __getitem__(self, item):
        return self.json[item]

    def dump(self):
        pass


class UserJson:
    def __init__(self, user_id: int):
        self.id = user_id
        self.json = json.load(open(str(os.getcwd()) + f"\\server\\profiles\\{user_id}.json"))

    def __getitem__(self, item):
        return self.json[item]

    def dump(self):
        json.dump(self.json, open(str(os.getcwd()) + f"\\server\\profiles\\{self.id}.json", "w"))
