"""These is the views file for party"""

from flask import Blueprint, request, make_response, jsonify
from ..models import office_model
office = office_model.OfficeModel()
office_route = Blueprint('office', __name__, url_prefix='/api/v1/offices') 

###create party
@office_route.route('', methods=['POST']) 
def create_chat_messages():
    """"This route enables admin user
      - to create political party"""
    
    data = request.get_json()
    type_data = data.get('type')
    name_data = data.get('name')
    
    if not type_data:
      return make_response(jsonify({
            "status": 400,
            "message": "type cannot be empty"
        })), 400

    if not name_data:
      return make_response(jsonify({
            "status": 400,
            "message": "Name cannot be empty"
        })), 400
    
    else:
        new_info = office.create_office(type_data, name_data)
        return make_response(jsonify({"status": 201,
                                      "data": [{
                                          "id": new_info["id"],
                                          "type": new_info["type"],
                                          "name": new_info["name"]
                                          }]})), 201


###Get all offices
@office_route.route('', methods=['GET']) 
def return_political_offices():
    """"This route enables citizen user
      - to view all political offices"""
    response = office.return_offices()
  
    return make_response(jsonify({"status": 200,
                                  "data": response
                                  })), 200

###Get individual office
@office_route.route('/<int:party_id>', methods=['GET']) 
def return_political_party(party_id):
    """"This route enables citizen user
      - to view individual political office"""
    response = office.find_office(party_id)
    if response:
      return make_response(jsonify({"status": 200,
                                  "data": [{
                                          "id": response[0]["id"],
                                          "type": response[0]["type"],
                                          "name": response[0]["name"]
                                          }]})), 200
    else:
       return make_response(jsonify({
            "status": 404,
            "message": "Office Id not found"
        })), 404
        