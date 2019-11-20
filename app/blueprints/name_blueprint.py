from flask import Blueprint
from flask import current_app
from flask import request
from ..models import Name
from lib.google_sheet_api.api_gateway import create_credentials
from lib.google_sheet_api.api_gateway import ApiGateway
import pdb
import json

name_blueprint = Blueprint('names', __name__, url_prefix='/names')


@name_blueprint.route('', methods=['POST'])
def create():
    name = Name(**request.form)
    dbsession = current_app.dbsession()
    dbsession.add(name)
    dbsession.commit()
    
    return 'test'

@name_blueprint.route("/<string:sheet_id>", methods=['PUT'])
def update_from_sheet(sheet_id):
    dbsession = current_app.dbsession()
    dbsession.query(Name).delete()
    dbsession.commit()
    
    g_sheet_api = ApiGateway(create_credentials())
    records = g_sheet_api.get_values(sheet_id, 'LastName', 1)
    last_names = list(map(lambda record: Name(**record), records))
    first_names = all_firstNames(sheet_id, g_sheet_api)

    dbsession.add_all(last_names + first_names)
    dbsession.commit()
    
    return 'ok'

def all_firstNames(sheet_id, api):
    records = api.get_values(sheet_id, 'FirstName_Animal', 1)
    records += api.get_values(sheet_id, 'FirstName_Personality', 1)
    records += api.get_values(sheet_id, 'FirstName_Random', 1)
    return list(map(lambda record: Name(**record), records))


@name_blueprint.route("", methods=['GET'])
def search_with_english_name():
    dbsession = current_app.dbsession()
    last_name = request.values['last_name'].lower()

    first_names = get_firstname(request.values['first_name'].lower(), dbsession)
    last_names = dbsession.query(Name).filter(Name.englished.like("{}%".format(last_name[0]))).all()

    return name_response(first_names, last_names)


import random

def name_response(first_names, last_names):
    last_name = random.sample(last_names, 1)[0]
    first_name = None
    text = None
    if first_names[0].category == 'random':
        first_name = random.sample(first_names, 1)[0]
        text = "{}, {}({})".format(first_name.traditional, last_name.traditional, last_name.englished)
    else:
        first_name = random.sample(first_names, 2)
        text = "{} {}, {}({})".format(first_name[0].traditional, first_name[1].traditional, last_name.traditional, last_name.englished)

    
    response = {
        "messages":[
            {
                "text": text
            }
        ]
    } 
    return response


import re

def get_firstname(first_name, dbsession):
    first_name_category = first_name
    if re.match(r"\d{4}", first_name):
        first_name_category = get_zodiac(int(first_name))
    
    first_names = dbsession.query(Name).filter(Name.category == first_name_category).all()

    return first_names



def get_zodiac(year):
    zodiac = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'goat', 'monkey', 'rooster', 'dog', 'pig']
    year = (year - 4) % 12
    return zodiac[year]