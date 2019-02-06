from flask import Flask, Blueprint, request, make_response, jsonify
from ..models import lobby_model
 
LOBBY = lobby_model.LobbyModel()
lobby_route = Blueprint('lobby', __name__,url_prefix='/api/v1/lobby') 
@lobby_route.route('',methods=['GET']) 
def get_lobby_messages():
    data = LOBBY.view_lobby_messages()
    return make_response(jsonify({
        "status": 200,
        "data": [{"message": data}]})), 200

@lobby_route.route('',methods=['POST']) 
def post_chat_messages():
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400
    chat = data.get('chat')
    LOBBY.add_chat_to_lobby(chat)
    return make_response(jsonify({
            "status": 201,
            "data": [{"message": "success"}]})), 201

