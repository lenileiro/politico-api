# -*- coding: utf-8 -*-
"""Office model.

This module helps data manipulation.
Officemodel class methods that manipulate the office data.
"""

# Mock data
DB = [
    {
        "id": 1,
        "type": 'county',
        "name": "mca"
    },
    {
        "id": 2,
        "type": 'county',
        "name": "woman Rep"
    },
    {
        "id": 3,
        "type": 'national',
        "name": "mp"
    }
]


class OfficeModel:
    """Office Model class"""

    def __init__(self):
        self.db = DB

    def find_office(self, oid: int) -> dict:
        """
        Finds a specific office
        Args:
        oid: Office Id.

        Returns:
            Returns office dictonary for office found
            Returns empty list for office not found.
        """

        return [office for office in self.db if office['id'] == oid]

    def create_office(self, otype: str, oname: str) -> dict:
        """
        Creates a new office
        Args:
        otype: Office Type.(National Government, County Government)
        oname: Office Name.

        Returns:
            The return office object created
        """
        office = {
            "id": len(self.db) + 1,
            "type": otype,
            "name": oname
            }
        self.db.append(office)
        return office

    def return_offices(self) -> dict:
        """
        Fetch all office object
        Returns:
            The return all office object
        """

        return self.db
