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

    def find_party(self, party_id):
        """receive the id
         -search if id is in the party_list
         -returns found data
         """
        party_found = [party for party in self.parties if party['id'] == party_id]
        return party_found

    def delete_party(self, party_id):
        """receive the id
        removes data on that id
        """
        self.parties.pop(party_id - 1)
    
    def edit_party(self, party_id, new_name):
        """update party information for particular ID"""
        value = self.parties.pop(int(party_id) - 1)
        del value['name']
        value.update({'name' : new_name})
        self.parties.insert(party_id - 1, value)
        return value
        
