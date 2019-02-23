# -*- coding: utf-8 -*-
"""Party model.

This module helps data manipulation.
PartyOffice class has multiple methods that manipulate,
the party data received from party views.
"""

# Mock data
DB = [
    {
        "id": 1,
        "name": 'party A',
        "hqAddress": 'box 432, Nairobi',
        "logoUrl": 'https://via.placeholder.com/150'
    },
    {
        "id": 2,
        "name": 'party B',
        "hqAddress": 'box 148, Nairobi',
        "logoUrl": 'https://via.placeholder.com/150'
    }
]


class PartyModel:
    """Office Model class"""

    def __init__(self):
        self.db = DB

    def find_party(self, pid: int) -> dict:
        """
        Finds a specific party

        Args:
        pid: party Id.

        Returns:
            Returns patry dictionary for party found
            Rerurns empty list for party not found.
        """

        party_found = [party for party in self.db if party['id'] == pid]
        return party_found

    def delete_party(self, pid: int):
        """
        Delete party from list

        Args:
        oid: party id.
        """
        self.db.pop(pid - 1)

    def edit_party(self, pid: int, pname: str) -> dict:
        """
        Edit a party's name

        Args:
        pid: Party ID.
        pname: Party Name.

        Returns:
            The return updated party dictionary
        """

        party = self.db.pop(int(pid) - 1)
        del party['name']
        party.update({'name': pname})
        self.db.insert(pid - 1, party)
        return party

    def create_party(self, pname: str, paddress: str, plogo: str) -> dict:
        """
        Creates a new party

        Args:
        pid: Party ID.
        pname: Party Name.

        Returns:
            The return updated party dictionary
        """

        new_party = {
            "id": len(self.db) + 1,
            "name": pname,
            "hqAddress": paddress,
            "logoUrl": plogo
            }

        self.db.append(new_party)
        return new_party

    def return_parties(self)-> dict:
        """
        Fetch all party object
        Returns:
            The return all party object
        """

        return self.db
