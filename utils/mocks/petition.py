
""""Votes Dummy data"""
from datetime import datetime

createdOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
petition_1 = {
    "v_id": 10,
    "createdOn":createdOn,
    "createdBy": 2,
    "v_office": 20001,
    "body": "rigging at the station"
}
petition_2 = {
    "v_id": 10,
    "createdOn":createdOn,
    "createdBy": 2,
    "v_office": 20002,
    "body": "fight at the polling station"
}