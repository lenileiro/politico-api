"""contains office logic"""
OFFICE = [
    {
        "id" : 1,
        "type" : 'county',
        "name": "mca"
    },
    {
        "id" : 2,
        "type" : 'county',
        "name": "woman Rep"
    },
    {
        "id" : 3,
        "type" : 'national',
        "name": "mp"
    }
]

class OfficeModel:
    """Office model class"""
    def __init__(self):
        self.office = OFFICE

    def find_office(self, office_id):
        """receive the id
         -search if id is in the office_list
         -returns found data
         """
        office_found = [office for office in self.office if office['id'] == office_id]
        return office_found

    def create_office(self, office_type, new_name):
        """creates new political office"""
        new_office = {
                "id" : len(self.office) + 1,
                "type" : office_type,
                "name" : new_name

            }

        self.office.append(new_office)
        return new_office
