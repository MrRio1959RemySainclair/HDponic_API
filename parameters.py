# people.py

from flask import make_response, abort
from config import db
from models import DATA, Datas_schema, Data_schema


def read_all():
    datas = DATA.query.all()
    return Datas_schema.dump(datas)

def read_one(Parameters):
    if Parameters in DATA:
        return DATA[Parameters]
    else:
        abort(
            404, f"Person with last name {Parameters} not found"
        )
'''
def update(Parameters, person):
    if Parameters in DATA:
        DATA[Parameters]["fname"] = person.get("fname", DATA[Parameters]["fname"])
        DATA[Parameters]["timestamp"] = get_timestamp()
        return DATA[Parameters]
    else:
        abort(
            404,
            f"Person with last name {Parameters} not found"
        )
'''        