import json
import os


class User:
    def __init__(self, user_id: int):
        self.id = user_id
        self.json = json.load(open(str(os.getcwd()) + f"\\server\\profiles\\{user_id}.json"))

    def __getitem__(self, item):
        return self.json[item]

    def dump(self):
        json.dump(self.json, open(str(os.getcwd()) + f"\\server\\profiles\\{self.id}.json", "w"))
