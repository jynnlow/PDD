from app.state.state import State
from app.models.user import User
from pprint import pprint
from datetime import date

class Appointment:
    __appointment_slot = {
        1: "0900 - 0930",
        2: "0930 - 1000",
        3: "1000 - 1030",
        4: "1030 - 1100",
        5: "1100 - 1130",
        6: "1130 - 1200",
        7: "1300 - 1330",
        8: "1300 - 1400",
        9: "1400 - 1430",
        10: "1430 - 1500",
        11: "1500 - 1530",
        12: "1530 - 1600",
        13: "1600 - 1630",
        14: "1630 - 1700",
        15: "1700 - 1730",
        16: "1730 - 1800"
    }

    def __init__(self,id, customer_name,customer_nric,dentist,treatment,date,timeslot,remark,status,user_id,cancel):
        self.id = id
        self.customer_name = customer_name
        self.customer_nric = customer_nric
        self.dentist = dentist
        self.treatment = treatment
        self.date = date
        self.timeslot = timeslot
        self.remark = remark
        self.status = status
        self.user_id = user_id
        self.cancel = cancel
 
    def createAppointment(date, timeslot):
        ableToCreate = True
        for appointment in State.getAppointmentList():
            if appointment.date == date and appointment.timeslot == timeslot:
                ableToCreate = False
                break
        
        newAppointment = Appointment()
        State.addAppointment(newAppointment)

        return ableToCreate

    def viewAppointmentsStatus(user_id):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.user_id == user_id:
                appointmentList.append(appointment)
        return appointmentList

    def cancelAppointment(appointment_id):
        cancelStatus = False
        currentDate = date.today()
        changeDateFormat = currentDate.strftime("%Y%m%d")
        for appointment in State.getAppointmentList():
            if appointment.id == appointment_id and appointment.status == "Pending" and appointment.date - changeDateFormat >= 1:
                appointment.cancel = True
                cancelStatus = True
                break
        return cancelStatus                

    def viewAppointmentsByStatusPending(status = "Pending"):  
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.status == status:
                appointmentList.append(appointment)
        return appointmentList
                           
    def updateAppointmentStatus(appointment_id,status):
         for appointment in State.getAppointmentList():
            if appointment.id == appointment_id:
                appointment.status = status
                break

    def insertRemark(appointment_id,remark):
        for appointment in State.getAppointmentList():
            if appointment.id == appointment_id:
                appointment.remark = remark
                break

    def generateAppointmentSummaryByCustomerName(customer_name):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.customer_name == customer_name:
                appointmentList.append(Appointment)
        return appointmentList

    def generateAppointmentSummaryByCustomerNRIC(customer_nric):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.customer_nric == customer_nric:
                appointmentList.append(Appointment)
        return appointmentList

    def generateAppointmentSummaryByDentistTreatment(treatment):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.treatment == treatment:
                appointmentList.append(Appointment)          
        return appointmentList 

    def getAppointmentSlotOptions():
        return Appointment.__appointment_slot

    def viewAppointmentsByDate():
        appointmentList = State.getAppointmentList()
        appointmentList.sort(key = lambda appointment: appointment.date)
        return appointmentList


    # LEARN FILTER FUNCTIONS
    # def filteredAppointmentsByDate(appointment):
    #             if appointment.date == date:
    #                 return True
    #             else:
    #                 return False

    #         filteredAppointmentList = filter(filteredAppointmentsByDate, State.getAppointmentList())
            
    #         def filteredAppoinmentsBySlot(appointment):
    #             if appointment.timeslot == timeslot:
    #                 return True
    #             else:
    #                 return False
            
    #         filteredAppointmentList = filter(filteredAppoinmentsBySlot, filteredAppointmentList)
            
    #         if len(list(filteredAppointmentList)) == 0:
    #             ableToCreate = True