from flask import make_response, abort
from config import db
from models import Datas, Datas_schema, HDponic_schema



# Fonction qui permet de lire toutes les donnees, les serialises et les envoient a l'API

def read_all():
    HDponic = Datas.query.all()
    return HDponic_schema.dump(HDponic)


# Foncton qui permet d'effectuer une recherche specifique

def read_one(Parameters):
    data = Datas.query.filter(Datas.Parameters == Parameters).one_or_none()

    if data is not None:
        return Datas_schema.dump(data)
    else:
        abort(404, f"Parameter with last name {Parameters} not found")

# 