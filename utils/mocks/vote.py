
""""Votes Dummy data"""
from datetime import datetime

createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
vote_1 = {
    "v_id": 10,
    "createdOn":createdOn,
    "createdBy": 2,
    "v_office": 20001,
    "c_candidate": 10001
}
vote_2 = {
    "v_id": 10,
    "createdOn":createdOn,
    "createdBy": 2,
    "v_office": 20002,
    "c_candidate": 10002
}