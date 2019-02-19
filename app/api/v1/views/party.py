from flask import Blueprint, request

from utils.serializer import Serializer as sp

from ..models.party import PartyModel


party = PartyModel()

bp = Blueprint('party-v1', __name__, url_prefix='/api/v1/parties') 


# delete party
@bp.route('/<int:party_id>', methods=['DELETE']) 
def delete_party(party_id):

    party_info = party.find_party(party_id)

    if party_info:
        party.delete_party(party_id)

        return sp.slist({"message": "delete successful"})

    else:
        return sp.slist({"message": "Party Id not found"}, 400)


# edit party
@bp.route('/<int:party_id>/name', methods=['PATCH'])
def edit_party(party_id):
    
    data = request.get_json()
    name_data = data.get('name')

    party_info = party.find_party(party_id)

    if not name_data:
        return sp.error("Name cannot be empty", 400)

    if party_info:
        new_info = party.edit_party(party_id, name_data)
        return sp.slist(
            {
                "id": party_id,
                "name": new_info["name"]
            })

    else:
        return sp.sdict({"message": "party not found"}, 404)


# create party
@bp.route('', methods=['POST'])
def create_party():

    data = request.get_json()
    name_data = data.get('name')
    address_data = data.get('hqAddress')
    logo_data = data.get('logoUrl')

    if not name_data:
        return sp.error("Name cannot be empty", 400)

    if not address_data:
        return sp.error("address cannot be empty", 400)

    if not logo_data:
        return sp.error("Logo cannot be empty", 400)

    else:

        new_info = party.create_party(name_data, address_data, logo_data)

        return sp.slist(
            {
                "id": new_info["id"],
                "name": new_info["name"]
            }, 201)


# Get all parties
@bp.route('/', methods=['GET'])
def return_parties():

    response = party.return_parties()

    return sp.sdict(response)


# Get individual parties
@bp.route('/<int:party_id>', methods=['GET']) 
def find_party(party_id):

    response = party.find_party(party_id)
    if response:
        return sp.slist({
                "id": response[0]["id"],
                "name": response[0]["name"],
                "logoUrl": response[0]["logoUrl"]})
    else:
        return sp.error(("Party Id not found"), 404)


