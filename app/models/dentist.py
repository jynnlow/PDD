from app.models.user import User
from app.models.worker import Worker

class Dentist(Worker):
    def __init__(self,id,username,password,fullName,nric,gender,contactNumber,address,role="dentist"):
        super().__init__(
            id = id,
            username = username,
            password = password,
            fullName = fullName,
            nric = nric,
            gender = gender,
            contactNumber = contactNumber, 
            address = address,
            role = role
        )

    def insertRemark():
        print("")