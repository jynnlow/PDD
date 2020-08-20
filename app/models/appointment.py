from app.state.state import State
from app.models.user import User
from pprint import pprint
from datetime import date, datetime, timedelta

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

    def __init__(self,customer_name,customer_nric,dentist,treatment,date,timeslot,user_id,status="Pending"):
        self.id = len(State.getAppointmentList())+1
        self.customer_name = customer_name
        self.customer_nric = customer_nric
        self.dentist = dentist
        self.treatment = treatment
        self.date = date
        self.timeslot = timeslot
        self.user_id = user_id
        self.status = status
        self.remark = ""
        self.cancel = False
 
    def createAppointment(customer_name,customer_nric,dentist,treatment,date,timeslot):
        ableToCreate = True
        for appointment in State.getAppointmentList():
            if appointment.date == date and appointment.timeslot == timeslot:
                ableToCreate = False
                break
        newAppointment = Appointment(customer_name,customer_nric,dentist,treatment,date,timeslot,State.getLogonUser()["user_id"])
        State.addAppointment(newAppointment)
        return ableToCreate

    def viewAppointmentsStatus(user_id):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.user_id == user_id:
                appointment_dict = {
                    "id": appointment.id,
                    "date": appointment.date,
                    "timeslot": Appointment.__appointment_slot[appointment.timeslot],
                    "dentist": appointment.dentist,
                    "treatment": appointment.treatment,
                    "status": appointment.status
                }
                appointmentList.append(appointment_dict)
        appointmentList.sort(key = lambda appointment: appointment["date"])
        return appointmentList

    def cancelAppointment(appointment_id):
        cancelStatus = False
        currentDate = datetime.now()
        for appointment in State.getAppointmentList():
            if appointment.id == int(appointment_id) and appointment.status == "Pending" and (datetime.strptime(str(appointment.date), "%Y%m%d") - currentDate).days >= 1:
                appointment.cancel = True
                cancelStatus = True
                break
        return cancelStatus

    def viewAppointmentsByStatusPending(status = "Pending"):  
        appointmentList = []
        for appointment in Appointment.view7daysAppointmentCalendar():
            if appointment["status"] == status:
                appointmentList.append(appointment)
        return appointmentList
                           
    def updateAppointmentStatus(appointment_id,status,remark = ""):
        appointmentList = []
        for appointment in State.getAppointmentList():
            if appointment.id == appointment_id:
                appointment.status = status
                appointment.remark = remark
                appointmentList.append()
                break 
        return appointmentList

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

    def getAppointmentSlotReverse():
        appointment_slot = {}
        i = 1
        while i <= 16 :
            appointment_slot[Appointment.__appointment_slot[i]] = i
            i+=1
        return appointment_slot

    def viewAppointmentsByDate(date):
        appointmentList = []
        for appointment in State.getAppointmentList():
                if appointment.date == date:
                    appointment_dict = vars(appointment)
                    appointment_dict["timeslot_time"] = Appointment.__appointment_slot[appointment.timeslot]
                    appointmentList.append(appointment_dict)
        appointmentList.sort(key = lambda appointment: appointment["date"])
        return appointmentList       

    def view7daysAppointmentCalendar():
        appointmentList = []
        for i in range (1,7):
            currentDay = int((date(2020,8,13) + timedelta(days=i)).strftime("%Y%m%d"))
            # currentDay = int((date.today() + timedelta(days=i)).strftime("%Y%m%d"))
            for appointment in State.getAppointmentList():
                if appointment.date == currentDay:
                    appointment_dict = vars(appointment)
                    appointment_dict["timeslot_time"] = Appointment.__appointment_slot[appointment.timeslot]
                    appointmentList.append(appointment_dict)
        appointmentList.sort(key = lambda appointment: appointment["date"])
        return appointmentList
        
    def viewTotalCustomersByTypes():
        totalCustomersByTypes = {
            "Extractions": [],
            "Fillings": [],
            "Repairs": [],
            "Teeth Cleaning": [],
            "Denture": []
        }
        returnData = []

        for appointment in State.getAppointmentList():
            if(appointment.user_id not in totalCustomersByTypes[appointment.treatment]):
                totalCustomersByTypes[appointment.treatment].append(appointment.user_id)
        
        for appointmentTypes in totalCustomersByTypes:
            returnData.append(
                {
                    "typeOfTreatment": appointmentTypes,
                    "customerCount": len(totalCustomersByTypes[appointmentTypes])
                }
            )
        return returnData

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