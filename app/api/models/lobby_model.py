from datetime import datetime
CHAT_LOBBY = []
class LobbyModel(object):
    def __init__(self):
        self.lobby = CHAT_LOBBY

    def add_chat_to_lobby(self,chat_message):
        chat = {
            'id': len(self.lobby) + 1,
            'chat': chat_message,
            'time': datetime.now()
            }
        self.lobby.append(chat)

    def view_lobby_messages(self):
        return self.lobby