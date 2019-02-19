# -*- coding: utf-8 -*-
"""Office View.

This module helps data manipulation.
PartyOffice class has multiple methods that manipulate,
the party data received from party views.
"""


from flask import Blueprint, request
from utils.serializer import Serializer as sp

from ..models.office import OfficeModel

office = OfficeModel()

bp = Blueprint('office-v1', __name__, url_prefix='/api/v1/offices') 


@bp.route('', methods=['POST']) 
def create_office():
    data = request.get_json()
    type_data = data.get('type')
    name_data = data.get('name')

    if not type_data:
        return sp.serialize_error("type cannot be empty", 400)

    if not name_data:
        return sp.serialize_error("Name cannot be empty", 400)

    else:
        new_info = office.create_office(type_data, name_data)
        return sp.serialize_object_list(
            {
                "id": new_info["id"],
                "type": new_info["type"],
                "name": new_info["name"]
            }, 201)


@bp.route('', methods=['GET'])
def return_offices():
    response = office.return_offices()

    return sp.serialize_object_dict(response)


@bp.route('/<int:party_id>', methods=['GET']) 
def find_office(party_id):

    response = office.find_office(party_id)
    if response:

        return sp.serialize_object_list(
            {
                "id": response[0]["id"],
                "type": response[0]["type"],
                "name": response[0]["name"]
            })

    else:
        return sp.serialize_error("Office Id not found", 400)