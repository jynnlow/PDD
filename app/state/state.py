class State:
    __userList = []
    __appointmentList = []
    __loginState = {
        "user_id" : 0,
        "message" : "",
        "role": ""
    }
    __cancelStatus = {
        "appointment_id" : 0,
        "message" : ""
    }

    def getUserList():
        return State.__userList
    
    def addUser(User):
        State.__userList.append(User)

    def logonUser(user_id, message, role):
        State.__loginState["user_id"] = user_id
        State.__loginState["message"] = message
        State.__loginState["role"] = role
    
    def getLogonUser():
        return State.__loginState

    def addAppointment(Appointment):
        State.__appointmentList.append(Appointment)

    def getAppointmentList():
        filteredAppointments = []
        for appointment in State.__appointmentList: 
            if appointment.cancel == False:
                filteredAppointments.append(appointment)
        return filteredAppointments

    def getAppointmentByID(appointment_ID):
        filteredAppointments = []
        for appointment in State.__appointmentList: 
            if appointment.cancel == False and appointment.id == appointment_ID:
                filteredAppointments.append(appointment)
        return filteredAppointments


   
    
        
    
