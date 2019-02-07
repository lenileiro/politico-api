"""These is the views file for party"""

from flask import Blueprint, make_response, jsonify
from ..models import party_model
PARTY = party_model.PartyModel()
parties_route = Blueprint('party', __name__, url_prefix='/api/v1/parties') 

###delete party
@parties_route.route('/<int:party_id>',methods=['DELETE']) 
def post_chat_messages(party_id):
    """"This route enables admin user
      - to delete party pass party id as parameter"""

    data = PARTY.delete_party(party_id)
    if data:
        return make_response(jsonify({"status": 200,
                                      "data": [{
                                          "message": "delete successful"}]})), 200
    else:
      return make_response(jsonify({"status": 400,
                                      "data": [{
                                          "message": "Id not found"}]})), 400

