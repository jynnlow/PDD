class State:
    __userList = []
    __appointmentList = []
    __loginState = {
        "user_id" : 0,
        "message" : ""
    }

    def getUserList():
        return State.__userList
    
    def addUser(User):
        State.__userList.append(User)

    def logonUser(user_id, message):
        State.__loginState["user_id"] = user_id
        State.__loginState["message"] = message
    
    def getLogonUser():
        return State.__loginState

    def addAppointment(Appointment):
        State.__appointmentList.append(Appointment)

    def getAppointmentList(user_id):
        return State.__appointmentList
        
