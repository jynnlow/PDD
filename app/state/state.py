class State:
    __userList = []
    __appointmentList = []
    __currentLogonUser = 0

    def getUserList():
        return State.__userList
    
    def addUser(User):
        State.__userList.append(User)

    def LogonUser(user_id):
        State.__currentLogonUser = user_id