from app.models.user import User

class Customer(User):
    def __init__(self,id,username,password,fullName,nric,gender,contactNumber,address,role="customer"):
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

    def makeAppointment():
        print("")

    #view for next seven days appointment
    def viewAppointmentCalender():
        print("")

    #together with appointment history
    def viewAppointmentStatus():
        print("")

    #at least one day before actual appointment date
    def cancelAppointment():
        print("")