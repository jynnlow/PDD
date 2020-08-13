from app.state.state import State
from app.models.user import User
class Appointment:
    def __init__(self,customerName,customerNRIC,dentist,treatment,date,time,remark,status,id):
        self.customerName = customerName
        self.customerNRIC = customerNRIC
        self.dentist = dentist
        self.treatment = treatment
        self.date = date 
        self.time = time 
        self.remark = remark
        self.status = status
        self.id = id

    def viewAppointmentCalendar():
        print("")
 
    def viewAppointmentStatus(id):
        for user in State.getAppointmentList(id):
            if user.id == id:
                return 

    def cancelAppointment():
        print("")

    def viewAppointment():
        print("")

    def updateAppointmentStatus():
        print("")

    def insertRemark():
        print("")

    def generateAppointmentSummary():
        print("")
