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

    def login (username,password):
        for user in State.getUserList():
            if user.username == username :
                if user.password == password:
                    State.logonUser(user.id, True)
                    break
                else: 
                    State.logonUser(0, False)
                    break
            else: 
                 State.logonUser(0, False)
        return State.getLogonUser()
        

    def logout():
        State.logonUser(0,False)
        return State.getLogonUser()

    def register (id,username,password,fullName,nric,gender,contactNumber,address,role):
        newUser = User(id,username,password,fullName,nric,gender,contactNumber,address,role)
        State.addUser(newUser)


    


