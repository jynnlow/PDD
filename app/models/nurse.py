from app.models.worker import Worker

class Nurse(Worker):
    def __init__(self,id,username,password,fullName,nric,gender,contactNumber,address,role="nurse"):
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

    def generateAppointmentSummary():
        print("")