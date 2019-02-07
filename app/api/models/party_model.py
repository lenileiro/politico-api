"""contains party logic"""
PARTIES = [
    {
        "id" : 1 ,
        "name" : 'party A' ,
        "hqAddress" : 'box 432, Nairobi' ,
        "logoUrl" : 'https://via.placeholder.com/150' 
    },
    {
        "id" : 2 ,
        "name" : 'party B' ,
        "hqAddress" : 'box 148, Nairobi' ,
        "logoUrl" : 'https://via.placeholder.com/150' 
    }
]

class PartyModel:
    """Party model class"""
    def __init__(self):
        self.parties = PARTIES

    def delete_party(self, party_id):
        """receive the id
         -search if id is in the party_list
         -returns found data
         """
        party_found = [party for party in self.parties if party['id'] == party_id]
        return party_found
        