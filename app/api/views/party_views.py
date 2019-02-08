"""These is the views file for party"""

from flask import Blueprint,request, make_response, jsonify
from ..models import party_model
party = party_model.PartyModel()
parties_route = Blueprint('party', __name__, url_prefix='/api/v1/parties') 

###delete party
@parties_route.route('/<int:party_id>',methods=['DELETE']) 
def delete_chat_messages(party_id):
    """"This route enables admin user
      - to delete party pass party id as parameter"""

    party_info = party.find_party(party_id)
    if party_info:
        party.delete_party(party_id)
        return make_response(jsonify({"status": 200 ,
                                      "data": [{
                                          "message": "delete successful"}]})), 200
    else:
        return make_response(jsonify({"status": 400,
                                      "data": [{
                                          "message": "Id not found"}]})), 400

###edit party
@parties_route.route('/<int:party_id>/name', methods=['PATCH']) 
def edit_chat_messages(party_id):
    """"This route enables admin user
      - to edit political party passing party id as parameter"""
    
    data = request.get_json()
    name_data = data.get('name')

    party_info = party.find_party(party_id)
    if party_info:
        new_info = party.edit_party(party_id, name_data)
        return make_response(jsonify({"status": 200,
                                      "data": [{
                                          "id": party_id,
                                          "name": new_info["name"]
                                          }]})), 200
    else:
      return make_response(jsonify({"status": 400,
                                      "data": [{
                                          "message": "Id not found"}]})), 400

###create party
@parties_route.route('', methods=['POST']) 
def create_chat_messages():
    """"This route enables admin user
      - to create political party"""
    
    data = request.get_json()
    name_data = data.get('name')
    address_data = data.get('hqAddress')
    logo_data = data.get('logoUrl')

    if name_data and address_data and logo_data:
        new_info = party.create_party(name_data, address_data, logo_data)
        return make_response(jsonify({"status": 200,
                                      "data": [{
                                          "id": new_info["id"],
                                          "name": new_info["name"]
                                          }]})), 200
    else:
      return make_response(jsonify({"status": 400,
                                      "data": [{
                                          "message": "some required fields missing"}]})), 400

