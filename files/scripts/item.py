import json
import os

from files.configs.items.associate_type import associate


def get_info_for_tpl(tpl):
    data = json.load(open(os.getcwd()+f"\\files\\configs\\items\\{associate[tpl]}\\{tpl}.json", encoding="utf-8"))
    return data

