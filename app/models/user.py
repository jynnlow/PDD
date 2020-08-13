from app.state.state import State

class User:
    def __init__(self,id,username,password,fullName,nric,gender,contactNumber,address,role):
        self.id = id
        self.username = username
        self.password = password
        self.fullName = fullName
        self.nric = nric
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address
        self.role = role

    def login (id,password):
        # is id and password correct?
        # if it's correct then
        State.LogonUser(id)

    def logout():
        State.LogonUser(0)
        print("")
    


