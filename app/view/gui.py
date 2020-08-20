from app.models.appointment import Appointment
from app.sharedkernel.general import General
from app.models.user import User
from tkinter import *
import tkinter as tk
from datetime import date

class DentistApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label_loginUsername = tk.Label(self, text = "Username:", font = ("Courier",15),fg = "black")
        label_loginPassword = tk.Label(self, text = "Password:", font = ("Courier",15),fg = "black")
        label_registerEmail = tk.Label(self, text = "Email:", font = ("Courier",15),fg = "black")
        label_registerPassword = tk.Label(self, text = "Password:", font = ("Courier",15),fg = "black")
        label_registerFullName = tk.Label(self, text = "Full Name:", font = ("Courier",15),fg = "black")
        label_registerNRIC = tk.Label(self, text = "IC Number:", font = ("Courier",15),fg = "black")
        label_registerGender = tk.Label(self, text = "Gender:", font = ("Courier",15),fg = "black")
        label_registerContact = tk.Label(self, text = "Contact Number:", font = ("Courier",15),fg = "black")
        label_registerAddress = tk.Label(self, text = "Address:", font = ("Courier",15),fg = "black")
        label_newUser = tk.Label(self, text = "New User?", font = ("Courier",25),fg = "grey") 
        label_ajustment = tk.Label(self, text = "         ")
        entry_loginUsername = tk.Entry(self)
        entry_loginPassword = tk.Entry(self)
        entry_registerEmail = tk.Entry(self)
        entry_registerPassword = tk.Entry(self)
        entry_registerFullname = tk.Entry(self)
        entry_registerNRIC = tk.Entry(self)
        entry_registerContact = tk.Entry(self)
        entry_registerAddress = tk.Entry(self) 
        button_login = tk.Button(self, text = "  Login  ", font = ("Courier",15),fg = "black", height = 2, command = lambda: User.login(entry_loginUsername.get(), entry_loginPassword()))
        button_register = tk.Button(self, text = "  Register Here!   ", font = ("Courier",15),fg = "black", height = 2) 
        gender = tk.StringVar()
        radioButton_female = tk.Radiobutton(self, text = "Female              ", variable = gender, value = "Female")
        radioButton_male = tk.Radiobutton(self, text = "Male", variable = gender, value = "Male")  
        #widget positioning
        label_loginUsername.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 5)
        label_loginPassword.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 5)
        label_ajustment.grid(row = 1, column = 2, sticky = tk.N, padx =  10, pady = 5)
        label_newUser.grid(row = 3, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerEmail.grid(row = 4, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerPassword.grid(row = 5, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerFullName.grid(row = 6, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerNRIC.grid(row = 7, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerGender.grid(row = 8, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerContact.grid(row = 10, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_registerAddress.grid(row = 11, column = 0, sticky = tk.W, padx =  10, pady = 5)
        label_ajustment.grid(row = 11, column = 2, sticky = tk.N, padx =  10, pady = 5)
        entry_loginUsername.grid(row = 0, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_loginPassword.grid(row = 1, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerEmail.grid(row = 4, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerPassword.grid(row = 5, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerFullname.grid(row = 6, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerNRIC.grid(row = 7, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerContact.grid(row = 10, column = 1, sticky = tk.N, padx =  10, pady = 5)
        entry_registerAddress.grid(row = 11, column = 1, sticky = tk.N, padx =  10, pady = 5)  
        button_login.grid(row = 2, column = 3, sticky = tk.N, padx =  10, pady = 5) 
        button_register.grid(row = 12, column = 3, sticky = tk.N, padx =  10, pady = 5)   
        radioButton_female.grid(row = 8, column = 1, sticky = tk.W, padx =  10, pady = 5)
        radioButton_male.grid(row = 9, column = 1, sticky = tk.W, padx =  10, pady = 5)

class CustomerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #widget creation
        label_options = tk.Label(self, text = "Welcome! Please select your option:", font = ("Courier",18),fg = "grey")
        button_makeAppointment = tk.Button(self, text = "Make Appointment", font = ("Courier",18),fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(MakeAppointmentPage))
        button_viewApoointmentStatusHistory = tk.Button(self, text = "View Appointment Status & History", font = ("Courier",18),fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewAppointmentStatusPage))
        button_cancelAppointment = tk.Button(self, text = "Cancel Appointment", font = ("Courier",18),fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(CancelAppointmentPage))
        button_logout = tk.Button(self, text = "Logout", font = ("Courier",15), fg = "grey", height = 2, width = 7, command = lambda: master.switch_frame(MainPage))
        label_ajustment = tk.Label(self, text = "                  ")
        #widget positioning
        label_options.grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_makeAppointment.grid(row = 3, column = 1, sticky = tk.N, padx = 10, pady = 15)
        button_viewApoointmentStatusHistory.grid(row = 4, column = 1, sticky = tk.N, padx = 10, pady = 15)
        button_cancelAppointment.grid(row = 5, column = 1, sticky = tk.N, padx = 10, pady = 15)
        label_ajustment.grid(row = 1, column = 0, sticky = tk.N, padx =  10, pady = 5)
        button_logout.grid(row = 6, column = 1, sticky = tk.W, padx = 10, pady = 15)

class MakeAppointmentPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        treatments = ["Extractions", "Fillings", "Repairs", "Teeth Cleaning", "Denture"]
        datelist = General.get7DaysByToday()
        timeslot = Appointment.getAppointmentSlotReverse()

        appointment_treatment = StringVar()
        appointment_treatment.set("Please select your treatment")
        appointment_date = IntVar()
        appointment_date.set("Please select your date")
        appointment_timeslot = StringVar()
        appointment_timeslot.set("Please select your timeslot")
        appointment_dentist = StringVar()
        appointment_dentist.set("Please select your dentist")

        # def printout(): 
        #     print(entry_appointmentName.get())
        #     print(entry_apopintmentNRIC.get())
        #     print(appointment_treatment.get())
        #     print(appointment_date.get())
        #     print(timeslot[appointment_timeslot.get()])
        #     print(appointment_dentist.get())

        #widget creation
        label_createAppointment = tk.Label(self, text = "Make Appointment", font = ("Courier",20),fg = "grey")
        label_appoinmentName = tk.Label(self, text = "Name:", font = ("Courier",17),fg = "black")
        label_appointmentNRIC = tk.Label(self, text = "IC Number:", font = ("Courier",17),fg = "black")
        label_appointmentTreatment = tk.Label(self, text = "Type of treatment:", font = ("Courier",17),fg = "black")
        label_appointmentDate = tk.Label(self, text = "Appointment Date:", font = ("Courier",17),fg = "black")
        label_appointmentTime = tk.Label(self, text = "Appointment Time:", font = ("Courier",17),fg = "black")
        label_appointmentDentist = tk.Label(self, text = "Dentist:", font = ("Courier",17),fg = "black")
        label_dateAlert = tk.Label(self, text = "*Can only make appointment within next 7 days.", font = ("Courier",10),fg = "red")
        label_timeAlert = tk.Label(self, text = "*Check for appointment calendar before select timeslot.", font = ("Courier",10),fg = "red")
        entry_appointmentName = tk.Entry(self)
        entry_apopintmentNRIC = tk.Entry(self)
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 5, command = lambda: master.switch_frame(CustomerPage))
        button_appointmentCalendar = tk.Button(self, text = "Next 7 Days Appointment Calendar", font = ("Courier",12), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(CalendarPage))
        optionMenu_appointmentTreatment = OptionMenu(self, appointment_treatment, *treatments)
        optionMenu_appointmentDate = OptionMenu(self, appointment_date, *datelist)
        optionMenu_appointmentTimeslot = OptionMenu(self, appointment_timeslot, *timeslot.keys())
        optionMenu_appointmentDentist = OptionMenu(self, appointment_dentist, "Dr.Stanley", "Dr.Ong")
        label_ajustment = tk.Label(self, text = "        ")
        #widget positioning
        label_createAppointment.grid (row = 0, column = 1, sticky = tk.W, padx = 10, pady = 10)
        label_ajustment.grid(row = 1, column = 0, sticky = tk.N, padx =  2)
        label_appoinmentName.grid(row = 2, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentNRIC.grid(row = 3, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentTreatment.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentDentist.grid(row = 5, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentDate.grid(row = 6, column = 1, sticky = tk.W, padx = 15, pady = 0)
        label_dateAlert.grid (row = 7, column = 1, sticky= tk.W, padx = 15, pady = 0)
        label_appointmentTime.grid(row = 8, column = 1, sticky = tk.W, padx = 15, pady = 0)
        label_timeAlert.grid (row = 9, column = 1, sticky= tk.W, padx = 15, pady = 0)  
        entry_appointmentName.grid(row = 2, column = 2, sticky = tk.W, padx = 15, pady = 10)
        entry_apopintmentNRIC.grid(row = 3, column = 2, sticky = tk.W, padx = 15, pady = 10)
        optionMenu_appointmentTreatment.grid(row = 4, column = 2, sticky = tk.W, padx = 15, pady = 10)
        optionMenu_appointmentDentist.grid(row = 5, column = 2, sticky = tk.W, padx = 15, pady = 10)
        optionMenu_appointmentDate.grid(row = 6, column = 2, sticky = tk.W, padx = 15, pady = 15)
        optionMenu_appointmentTimeslot.grid(row = 8, column = 2, sticky = tk.W, padx = 15, pady = 15)       
        label_ajustment.grid(row = 11, column = 1, sticky = tk.N, padx = 2)
        label_ajustment.grid(row = 11, column = 3, sticky = tk.N, padx = 2)
        button_appointmentCalendar.grid(row = 10, column = 1, sticky = tk.W, padx = 15, pady = 10)
        button_submitAppointment.grid(row = 12, column = 2, sticky = tk.N, padx = 15, pady = 10)
        button_back.grid(row = 12, column = 1, sticky = tk.W, padx = 15, pady = 10)

class ViewAppointmentStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #widget creation
        label_viewAppointmentStatus  = tk.Label(self, text = "View Appointment Status & History", font = ("Courier",20),fg = "grey")
        text_viewAppointmentStatus = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 23, width = 71)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(CustomerPage))
        #widget positioning 
        label_viewAppointmentStatus.grid (row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        text_viewAppointmentStatus.grid(row = 1, column = 0, sticky = tk.N, padx = 10, pady = 10)
        button_back.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)

class CancelAppointmentPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #widget creation
        label_cancelAppointment = tk.Label(self, text = "Cancel Appointment", font = ("Courier",20),fg = "grey")
        label_cancelAppointmentInfo = tk.Label(self, text = "Please enter the appointment id that you wish to cancel: ",font = ("Courier",17),fg = "black" )
        label_cancelAppointmentAlert = tk.Label(self, text = "*You can only cancel the appointment at least one day before the appointment date.",font = ("Courier",12),fg = "red" )
        label_cancelAppointmentAlert2 = tk.Label(self, text = "*You can only cancel the appointment that is still pending. ",font = ("Courier",12),fg = "red" )
        entry_cancelApointmentID = tk.Entry(self)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(CustomerPage))
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8)
        label_ajustment = tk.Label(self, text = "           ")
        #widget positioning 
        label_cancelAppointment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 10)
        label_cancelAppointmentInfo.grid(row = 1, column = 0, sticky = tk.W, padx = 15, pady = 10 )
        entry_cancelApointmentID.grid(row = 5, column = 0, sticky = tk.N, padx = 15, pady = 10)
        label_cancelAppointmentAlert.grid(row = 2, column = 0, sticky = tk.W, padx = 15, pady = 0)
        label_cancelAppointmentAlert2.grid(row = 3, column = 0, sticky = tk.W, padx = 15, pady = 10)
        label_ajustment.grid(row = 4, column = 0, sticky = tk.W, padx = 15, pady = 10)
        label_ajustment.grid(row = 6, column = 0, sticky = tk.W, padx = 15, pady = 10)
        label_ajustment.grid(row = 7, column = 0, sticky = tk.W, padx = 15, pady = 10)
        button_back.grid(row = 8, column = 0, sticky = tk.W, padx = 15, pady = 10)
        button_submitAppointment.grid(row = 8, column = 0, sticky = tk.E, padx = 15, pady = 10)

class CalendarPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_viewAppointmentCalendar = tk.Label(self, text = "Next 7 Days Appointment Calender", font = ("Courier",20),fg = "grey")
        text_viewAppointmentCalendar = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 23, width = 71)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(MakeAppointmentPage))
        #Widget Positioning 
        label_viewAppointmentCalendar.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        text_viewAppointmentCalendar.grid(row = 1, column = 0, sticky = tk.N, padx = 10, pady = 10)
        button_back.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)

class DentistPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_dentistPage = tk.Label(self, text = "Dentist Page", font = ("Courier",20),fg = "grey")
        button_viewAllAppointment = tk.Button(self, text = "View All Appointment", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewAllAppointmentPage))
        button_viewPendingAppointment = tk.Button(self, text = "View Pending Appointment", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewPendingAppointmentPage))
        button_updateAppointmentStatus = tk.Button(self, text = "Update Appointment Status", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(UpdateAppointmentStatusPage))
        button_viewAppointmentByDay = tk.Button(self, text = "View Appointment(By Day)", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewAppointmentByDatePage))
        label_ajustment = tk.Label(self, text = "                        ")
        button_logout = tk.Button(self, text = "Logout", font = ("Courier",15), fg = "grey", height = 2, width = 7, command = lambda: master.switch_frame(MainPage))
        #widget Positioning
        label_ajustment.grid(row = 0, column = 0)
        label_dentistPage.grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_viewAllAppointment.grid(row = 2, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_viewPendingAppointment.grid(row = 3, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_updateAppointmentStatus.grid(row = 5, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_viewAppointmentByDay.grid(row = 4, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_logout.grid(row = 6, column = 1, sticky = tk.W, padx = 10, pady = 15)

class ViewPendingAppointmentPage(tk.Frame):
     def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_viewPendingAppointment = tk.Label(self, text = "View Next 7 Days Pending Appointment", font = ("Courier",20),fg = "grey")
        text_viewPendingAppointment = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 23, width = 71)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))        
        #Widget Positioning
        label_viewPendingAppointment.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        text_viewPendingAppointment.grid(row = 1, column = 0, sticky = tk.N, padx = 10, pady = 10)
        button_back.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)
        
class ViewAllAppointmentPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_viewPendingAppointment = tk.Label(self, text = "View All Appointment", font = ("Courier",20),fg = "grey")
        text_viewPendingAppointment = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 23, width = 71)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))        
        #Widget Positioning
        label_viewPendingAppointment.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        text_viewPendingAppointment.grid(row = 1, column = 0, sticky = tk.N, padx = 10, pady = 10)
        button_back.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)

class UpdateAppointmentStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        updateStatus = StringVar()
        updateStatus.set("Pending")
        #Widget Creation
        label_updateAppointmentStatus = tk.Label(self, text = "Update Appointment Status", font = ("Courier",20),fg = "grey")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_ajustment = tk.Label(self, text = "")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Confirmed", "Rejected")
        label_remark = tk.Label(self, text = "Remark: ", font = ("Courier",14),fg = "black")
        text_remark = tk.Text(self, font = ("Courier",15),bg = "#EBECF0", height = 3, width = 60)
        text_viewPendingAppointment = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 12, width = 60)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))       
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8)
        #widget Positioning
        label_updateAppointmentStatus.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_updateAppointmentStatusIDInfo.grid(row = 2, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(row = 3, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(row = 3, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_updatedStatus.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(row = 4, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_remark.grid(row = 5, column = 1, sticky = tk.W, padx = 15, pady = 5)
        text_remark.grid(row = 6, column = 1, sticky = tk.W, padx = 15, pady = 10)
        text_viewPendingAppointment.grid(row = 1, column = 1, sticky = tk.N, padx = 10, pady = 5)
        button_back.grid(row = 7, column = 1, sticky = tk.W, padx = 10, pady = 5)
        button_submitAppointment.grid(row = 7, column = 1, sticky = tk.E, padx = 10, pady = 5)

class ViewAppointmentByDatePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        updateStatus = StringVar()
        updateStatus.set("Status")
        #Widget Creation
        label_viewAppointmentStatusByDate = tk.Label(self, text = "View Appointment By Date", font = ("Courier",20),fg = "grey")
        label_viewAppointmentStatusByDateInfo = tk.Label(self, text = "Please enter a date that you wish to view and update: ",font = ("Courier",15),fg = "black" )
        entry_date = tk.Entry(self)   
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8)
        text_viewAppointmentByDate = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 12, width = 60) 
        label_ajustment = tk.Label(self, text = "")
        label_alert = tk.Label(self, text = "Date Format: YYYYMMDD (etc: 20200931)", font = ("Courier",10),fg = "red")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Completed", "No-show")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))       
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8)
        #widget positioning
        label_viewAppointmentStatusByDate.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_viewAppointmentStatusByDateInfo.grid(row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_date.grid(row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        button_submit.grid(row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)
        text_viewAppointmentByDate.grid(row = 4, column = 1, sticky = tk.N, padx = 10, pady = 5)
        label_alert.grid(row = 3, column = 1, sticky = tk.N, padx = 10, pady = 0)
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_updateAppointmentStatusIDInfo.grid(row = 5, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(row = 6, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(row = 6, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_updatedStatus.grid(row = 7, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(row = 7, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_ajustment.grid(row = 8, column = 0, sticky = tk.W, padx = 15, pady = 5)
        button_back.grid(row = 9, column = 1, sticky = tk.W, padx = 10, pady = 5)
        button_submitAppointment.grid(row = 9, column = 1, sticky = tk.E, padx = 10, pady = 5)

class OverwriteAppointmentStatus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        updateStatus = StringVar()
        updateStatus.set("Pending")
        #Widget Creation
        label_updateAppointmentStatus = tk.Label(self, text = "Overwrite Appointment Status", font = ("Courier",20),fg = "grey")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_ajustment = tk.Label(self, text = "")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Confirmed", "Rejected")
        text_viewPendingAppointment = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 15, width = 60)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8)
        #widget Positioning
        label_updateAppointmentStatus.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_updateAppointmentStatusIDInfo.grid(row = 2, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(row = 3, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(row = 3, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_updatedStatus.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(row = 4, column = 1, sticky = tk.N, padx = 15, pady = 5)
        text_viewPendingAppointment.grid(row = 1, column = 1, sticky = tk.N, padx = 10, pady = 5)
        label_ajustment.grid(row = 7, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_ajustment.grid(row = 7, column = 0, sticky = tk.E, padx = 15, pady = 5)
        button_back.grid(row = 8, column = 1, sticky = tk.W, padx = 10, pady = 5)
        button_submitAppointment.grid(row = 8, column = 1, sticky = tk.E, padx = 10, pady = 5)

class NursePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
         #Widget Creation
        label_dentistPage = tk.Label(self, text = "Nurse Page", font = ("Courier",20),fg = "grey")
        label_ajustment = tk.Label(self, text = "                        ")
        label_generateSummary = tk.Label(self, text = "Generate Summary: ", font = ("Courier",18),fg = "black")
        button_viewAllAppointment = tk.Button(self, text = "View All Appointment", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(ViewAllAppointmentPageNurse))
        button_overwriteAppointmentStatus = tk.Button(self, text = "Overwrite Appointment Status", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(OverwriteAppointmentStatus))
        button_generateSummaryByName = tk.Button(self, text = "By Customer's Name", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByName))
        button_generateSummaryByIC = tk.Button(self, text = "By Customer's NRIC", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByIC))
        button_generateSummaryByTreatment = tk.Button(self, text = "By Treatment Type", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByTreatment))
        button_logout = tk.Button(self, text = "Logout", font = ("Courier",15), fg = "grey", height = 2, width = 7, command = lambda: master.switch_frame(MainPage))
        #widget Positioning
        label_ajustment.grid(row = 0, column = 0)
        label_dentistPage.grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_viewAllAppointment.grid(row = 2, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_overwriteAppointmentStatus.grid(row = 3, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_generateSummaryByName.grid(row = 5, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_generateSummaryByIC.grid(row = 6, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_generateSummaryByTreatment.grid(row = 7, column = 1, sticky = tk.W, padx = 10, pady = 10)
        label_generateSummary.grid(row = 4, column = 1, sticky = tk.W, padx = 10, pady = 10)
        button_logout.grid(row = 8, column = 1, sticky = tk.W, padx = 10, pady = 10)

class GenerateSummaryByName(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_generateSummaryByName = tk.Label(self, text = "Generate Summary By Name", font = ("Courier",20),fg = "grey")
        label_generateSummaryByNameInfo = tk.Label(self, text = "Please enter a name that you wish to search: ",font = ("Courier",15),fg = "black" )
        entry_customerName = tk.Entry(self)   
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8)
        text_generateSummaryByName = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 20, width = 60) 
        label_ajustment = tk.Label(self, text = "")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        #Widget Positioning
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByName.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByNameInfo.grid(row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_customerName.grid(row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        button_back.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        text_generateSummaryByName.grid(row = 3, column = 1, sticky = tk.N, padx = 10, pady = 5)
        button_submit.grid(row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)

class GenerateSummaryByIC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_generateSummaryByIC = tk.Label(self, text = "Generate Summary By NRIC", font = ("Courier",20),fg = "grey")
        label_generateSummaryByICInfo = tk.Label(self, text = "Please enter NRIC number that you wish to search: ",font = ("Courier",15),fg = "black" )
        entry_customerIC = tk.Entry(self)   
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8)
        text_generateSummaryByName = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 20, width = 60) 
        label_ajustment = tk.Label(self, text = "")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        #Widget Positioning
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByIC.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByICInfo.grid(row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_customerIC.grid(row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        button_back.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        text_generateSummaryByName.grid(row = 3, column = 1, sticky = tk.N, padx = 10, pady = 5)
        button_submit.grid(row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)

class GenerateSummaryByTreatment(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        treatments = ["Extractions", "Fillings", "Repairs", "Teeth Cleaning", "Denture"]
        appointment_treatment = StringVar()
        appointment_treatment.set("Please select your treatment")
        #Widget Creation
        label_generateSummaryByTreatment = tk.Label(self, text = "Generate Summary By Treatment Type", font = ("Courier",20),fg = "grey")
        label_generateSummaryByTreatmentInfo = tk.Label(self, text = "Please select treatment type that you wish to search: ",font = ("Courier",15),fg = "black" )
        optionMenu_appointmentTreatment = OptionMenu(self, appointment_treatment, *treatments)
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8)
        text_generateSummaryByName = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 20, width = 60) 
        label_ajustment = tk.Label(self, text = "")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        #Widget Positioning
        label_ajustment.grid(row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByTreatment.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByTreatmentInfo.grid(row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        optionMenu_appointmentTreatment.grid(row = 2, column = 1, sticky = tk.S, padx = 15, pady = 10)
        button_back.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        text_generateSummaryByName.grid(row = 3, column = 1, sticky = tk.N, padx = 10, pady = 5)
        button_submit.grid(row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)

class ViewAllAppointmentPageNurse(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_viewPendingAppointment = tk.Label(self, text = "View All Appointment", font = ("Courier",20),fg = "grey")
        text_viewPendingAppointment = tk.Text(self, font = ("Courier",15),bg = "#EEEEEE", height = 23, width = 71)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))        
        #Widget Positioning
        label_viewPendingAppointment.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        text_viewPendingAppointment.grid(row = 1, column = 0, sticky = tk.N, padx = 10, pady = 10)
        button_back.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 10)




def main():
    app = DentistApp()
    app.title('Oriental Dentist Clinic')
    app.geometry("670x530")
    app.mainloop()