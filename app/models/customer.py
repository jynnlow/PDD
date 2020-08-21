from app.models.user import User
from app.state.state import State

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

    def getCustomerDetailsByID():
        full_name = ""
        nric = 0
        user_id = State.getLogonUser()["user_id"]
        for user in State.getUserList():
            if user.id == user_id:
                full_name = user.fullName
                nric = user.nric
        return full_name, nric

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

    def register (id,username,password,fullName,nric,gender,contactNumber,address, role = "Customer"):
        newUser = User(id,username,password,fullName,nric,gender,contactNumber,address, role)
        State.addUser(newUser)
