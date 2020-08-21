from pprint import pprint
from mocks.appointment import AppointmentMock
from app.state.state import State
from app.models.appointment import Appointment
from app.models.customer import Customer
from app.sharedkernel.general import General
from app.models.user import User
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import date

class DentistApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(GenerateSummaryByIC)

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
        button_login = tk.Button(self, text = "  Login  ", font = ("Courier",15),fg = "black", height = 2, command = lambda: self.login(master, entry_loginUsername.get(), entry_loginPassword.get()))
        button_register = tk.Button(self, text = "  Register Here!   ", font = ("Courier",15),fg = "black", height = 2, command = lambda: self.registerUser(master, entry_registerEmail.get(), entry_registerPassword.get(), entry_registerFullname.get(),entry_registerNRIC.get(), gender.get(),entry_registerContact.get(), entry_registerAddress.get(), role = "Customer")) 
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

    def login(self, master, username, password):
        loginResult = User.login(username, password)
        if loginResult["message"] == True:
            if loginResult["role"] == "dentist":
                master.switch_frame(DentistPage)
            elif loginResult["role"] == "nurse":
                master.switch_frame(NursePage)
            else: 
                master.switch_frame(CustomerPage)
        else: 
            messagebox.showerror("LOGIN FAILED", "Please make sure you type in the correct username and password!")

    def registerUser(self, master, username, password, fullName, nric, gender,contactNumber, address, role):
        user_id = len(State.getUserList())
        Customer.register(user_id,username,password,fullName,nric,gender,contactNumber,address, role)
           
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

        #widget creation
        label_createAppointment = tk.Label(self, text = "Make Appointment", font = ("Courier",20),fg = "grey")
        label_appointmentTreatment = tk.Label(self, text = "Type of treatment:", font = ("Courier",17),fg = "black")
        label_appointmentDate = tk.Label(self, text = "Appointment Date:", font = ("Courier",17),fg = "black")
        label_appointmentTime = tk.Label(self, text = "Appointment Time:", font = ("Courier",17),fg = "black")
        label_appointmentDentist = tk.Label(self, text = "Dentist:", font = ("Courier",17),fg = "black")
        label_dateAlert = tk.Label(self, text = "*Can only make appointment within next 7 days.", font = ("Courier",10),fg = "red")
        label_timeAlert = tk.Label(self, text = "*Check for appointment calendar before select timeslot.", font = ("Courier",10),fg = "red")
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: self.makeAppointment(appointment_dentist.get(), appointment_treatment.get(),appointment_date.get(),timeslot[appointment_timeslot.get()]))
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
        label_appointmentTreatment.grid(row = 4, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentDentist.grid(row = 5, column = 1, sticky = tk.W, padx = 15, pady = 10)
        label_appointmentDate.grid(row = 6, column = 1, sticky = tk.W, padx = 15, pady = 0)
        label_dateAlert.grid (row = 7, column = 1, sticky= tk.W, padx = 15, pady = 0)
        label_appointmentTime.grid(row = 8, column = 1, sticky = tk.W, padx = 15, pady = 0)
        label_timeAlert.grid (row = 9, column = 1, sticky= tk.W, padx = 15, pady = 0)  
        optionMenu_appointmentTreatment.grid(row = 4, column = 2, sticky = tk.W, padx = 15, pady = 10)
        optionMenu_appointmentDentist.grid(row = 5, column = 2, sticky = tk.W, padx = 15, pady = 10)
        optionMenu_appointmentDate.grid(row = 6, column = 2, sticky = tk.W, padx = 15, pady = 15)
        optionMenu_appointmentTimeslot.grid(row = 8, column = 2, sticky = tk.W, padx = 15, pady = 15)       
        label_ajustment.grid(row = 11, column = 1, sticky = tk.N, padx = 2)
        label_ajustment.grid(row = 11, column = 3, sticky = tk.N, padx = 2)
        button_appointmentCalendar.grid(row = 10, column = 1, sticky = tk.W, padx = 15, pady = 10)
        button_submitAppointment.grid(row = 12, column = 2, sticky = tk.N, padx = 15, pady = 10)
        button_back.grid(row = 12, column = 1, sticky = tk.W, padx = 15, pady = 10)

    def makeAppointment(self,dentist,treatment,date,timeslot):
        customer_name, customer_nric = Customer.getCustomerDetailsByID()
        result = Appointment.createAppointment(
            customer_name=customer_name,
            customer_nric=customer_nric,
            dentist=dentist,
            treatment=treatment,
            date=date,
            timeslot=timeslot,
        )       
        if result == True:
            messagebox.showinfo("SUCCESSFUL", "Congratulation! Your appointment is successfully made!")
        else: 
            messagebox.showerror("MAKE APPOINTMENT FAILED", "Error: Only allowed book an appointment timeslot that is haven't booked by other customer. (refer to calendar)")

class ViewAppointmentStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        user_id = State.getLogonUser()["user_id"]
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot": "Time Slot",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status"
            }
        ]
        data.extend(Appointment.viewAppointmentsStatus(user_id))
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                self.e.grid(row=i+1, column=k, sticky = tk.W)
                self.e.insert(tk.INSERT, data[i][j])
                self.e.configure(state="readonly")
                k+=1

        #widget creation
        button_back = tk.Button(self, text = "Back", font = ("Courier",11), fg = "grey", height = 1, width = 6, command = lambda: master.switch_frame(CustomerPage))
        #widget positioning 
        label_viewAppointmentStatus  = tk.Label(self, text = "View Appointment Status & History", font = ("Courier",20),fg = "grey")
        label_viewAppointmentStatus.grid (columnspan=6, row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        button_back.grid(row = len(data)+2, column = 0, sticky = tk.W, padx = 10, pady = 10)

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
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: self.cancelAppointment(entry_cancelApointmentID.get()))
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

    def cancelAppointment(self, appointment_id):
        cancelResult = Appointment.cancelAppointment(appointment_id)
        if cancelResult == True:
            messagebox.showinfo("SUCCESSFUL", "Congratulation! Your appointment is cancel successfully!")
        else: 
            messagebox.showerror("FAILED", "Cancel unsuccessful. Please check on the criteria above. (with red)")

class CalendarPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        data = [
            {
                "customer_name": "Customer Name",
                "date": "Date",
                "dentist": "Dentist",
                "timeslot_time": "Time Slot"
            }
        ]
        data.extend(Appointment.view7daysAppointmentCalendar())
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "customer_name" or j == "date" or j == "dentist" or j == "timeslot_time" or j == "status":
                    self.e.grid(row=i+1, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1
        #Widget Creation
        label_viewAppointmentCalendar = tk.Label(self, text = "Next 7 Days Appointment Calender", font = ("Courier",20),fg = "grey")
        button_back = tk.Button(self, text = "Back", font = ("Courier",11), fg = "grey", height = 1, width = 6, command = lambda: master.switch_frame(MakeAppointmentPage))
        #Widget Positioning 
        label_viewAppointmentCalendar.grid(columnspan= 4, row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        button_back.grid(row = len(data)+2, column = 0, sticky = tk.W, padx = 10, pady = 10)

class DentistPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_dentistPage = tk.Label(self, text = "Dentist Page", font = ("Courier",20),fg = "grey")
        button_viewPendingAppointment = tk.Button(self, text = "View Pending Appointment", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewPendingAppointmentPage))
        button_updateAppointmentStatus = tk.Button(self, text = "Update Appointment Status", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(UpdateAppointmentStatusPage))
        button_viewAppointmentByDay = tk.Button(self, text = "View Appointment(By Day)", font = ("Courier",18), fg = "black", height = 3, width = 40, command = lambda: master.switch_frame(ViewAppointmentByDatePage))
        label_ajustment = tk.Label(self, text = "                        ")
        button_logout = tk.Button(self, text = "Logout", font = ("Courier",15), fg = "grey", height = 2, width = 7, command = lambda: master.switch_frame(MainPage))
        #widget Positioning
        label_ajustment.grid(row = 0, column = 0)
        label_dentistPage.grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_viewPendingAppointment.grid(row = 3, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_updateAppointmentStatus.grid(row = 5, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_viewAppointmentByDay.grid(row = 4, column = 1, sticky = tk.W, padx = 10, pady = 15)
        button_logout.grid(row = 6, column = 1, sticky = tk.W, padx = 10, pady = 15)

class ViewPendingAppointmentPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.viewAppointmentsByStatusPending())
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+1, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1

        #Widget Creation
        label_viewPendingAppointment = tk.Label(self, text = "View Next 7 Days Pending Appointment", font = ("Courier",20),fg = "grey")
        button_back = tk.Button(self, text = "Back", font = ("Courier",12), fg = "grey", height = 1, width = 6, command = lambda: master.switch_frame(DentistPage))        
        #Widget Positioning
        label_viewPendingAppointment.grid(columnspan = 7, row = 0, column = 0, sticky = tk.W, padx = 10, pady = 10)
        button_back.grid(row = len(data)+2, column = 0, sticky = tk.W, padx = 10, pady = 10)
        
class UpdateAppointmentStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.viewAppointmentsByStatusPending())
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+1, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1
        updateStatus = StringVar()
        updateStatus.set("Pending")
        #Widget Creation
        label_updateAppointmentStatus = tk.Label(self, text = "Update Appointment Status", font = ("Courier",20),fg = "grey")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_ajustment = tk.Label(self, text = "    ")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Confirmed", "Rejected")
        label_remark = tk.Label(self, text = "Remark: ", font = ("Courier",14),fg = "black")
        entry_remark = tk.Entry(self)
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))       
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: self.submitID(int(entry_updateApointmentStatusID.get()), updateStatus.get(),entry_remark.get()))
        #widget Positioning
        label_updateAppointmentStatus.grid(columnspan = 7,row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_updateAppointmentStatusIDInfo.grid(columnspan = 7,row = len(data)+2, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(columnspan = 7,row = len(data)+3, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(columnspan = 7,row = len(data)+3, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_ajustment.grid(columnspan = 7,row = len(data), column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_updatedStatus.grid(columnspan = 7,row = len(data)+4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(columnspan = 7,row = len(data)+4, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_remark.grid(columnspan = 7,row = len(data)+5, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_remark.grid(columnspan = 7,row = len(data)+5, column = 1, sticky = tk.N, padx = 15, pady = 10)
        button_back.grid(columnspan = 7,row = len(data)+7, column = 1, sticky = tk.W, padx = 10, pady = 5)
        button_submitAppointment.grid(columnspan = 7,row = len(data)+7, column = 1, sticky = tk.E, padx = 10, pady = 5)

    def submitID(self, appointment_id, status, remark):
        appointmentList = Appointment.viewAppointmentsByStatusPending()
        for appointment in appointmentList:
           if appointment["id"] == appointment_id:
                Appointment.updateAppointmentStatus(appointment_id,status,remark)
                messagebox.showinfo("SUCCESS", "Update Successfully")
                break
        else:
            messagebox.showinfo("FAILED", "Please make you insert correct appointment id (must be pending appointment!")

class ViewAppointmentByDatePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_viewAppointmentStatusByDate = tk.Label(self, text = "View Appointment By Date", font = ("Courier",20),fg = "grey")
        label_viewAppointmentStatusByDateInfo = tk.Label(self, text = "Please enter a date that you wish to view and update: ",font = ("Courier",15),fg = "black" )
        entry_date = tk.Entry(self)   
        label_alert = tk.Label(self, text = "Date Format: YYYYMMDD (etc: 20200931)", font = ("Courier",10),fg = "red")
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: self.submitDate(master, int(entry_date.get())))
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(DentistPage))       
        #widget positioning
        label_viewAppointmentStatusByDate.grid(columnspan=5, row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_viewAppointmentStatusByDateInfo.grid(columnspan=5, row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_date.grid(columnspan=5, row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        label_alert.grid(columnspan=5, row = 3, column = 1, sticky = tk.N, padx = 10, pady = 0)
        button_submit.grid(columnspan=5, row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)
        button_back.grid(columnspan=5, row = 4, column = 1, sticky = tk.W, padx = 10, pady = 5)

    def submitDate(self, master, date):
        result = Appointment.appointmentDate(date)
        if result == False:
            messagebox.showinfo("FAILED", "Date does not exists!")
        else: 
            self.updatePanel(master,date)

    def updatePanel(self, master, date):
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.viewAppointmentsByDate(int(date)))
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+6, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1

        updateStatus = StringVar()
        updateStatus.set("Status")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Completed", "No-show")
        
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: Appointment.updateAppointmentStatus(int(entry_updateApointmentStatusID.get()), updateStatus.get())) 
        label_updateAppointmentStatusIDInfo.grid(columnspan=5, row = len(data)+7, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(columnspan=5, row = len(data)+8, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(columnspan=5, row = len(data)+8, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_updatedStatus.grid(columnspan=5, row = len(data)+9, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(columnspan=5, row = len(data)+9, column = 1, sticky = tk.N, padx = 15, pady = 5)        
        button_submitAppointment.grid(columnspan=5, row = len(data)+11, column = 1, sticky = tk.E, padx = 10, pady = 5)

class OverwriteAppointmentStatus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.viewAppointmentsByStatusPending())
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+1, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1
        updateStatus = StringVar()
        updateStatus.set("Pending")
        #Widget Creation
        label_updateAppointmentStatus = tk.Label(self, text = "Overwrite Appointment Status", font = ("Courier",20),fg = "grey")
        label_updateAppointmentStatusIDInfo = tk.Label(self, text = "Please enter the appointment id that you wish to update: ",font = ("Courier",15),fg = "black" )
        label_updateAppointmentStatusID = tk.Label(self, text = "Appointment ID: ", font = ("Courier",14),fg = "black")
        label_updatedStatus = tk.Label(self, text = "Updated Status: ", font = ("Courier",14),fg = "black")
        entry_updateApointmentStatusID = tk.Entry(self)    
        label_ajustment = tk.Label(self, text = "    ")
        optionMenu_updateStatus = OptionMenu(self, updateStatus, "Confirmed", "Rejected")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        button_submitAppointment = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 2, width = 8, command = lambda: self.submitID(int(entry_updateApointmentStatusID.get()), updateStatus.get()))
        #widget Positioning
        label_updateAppointmentStatus.grid(columnspan = 7,row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_updateAppointmentStatusIDInfo.grid(columnspan = 7,row = len(data)+2, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        label_updateAppointmentStatusID.grid(columnspan = 7,row = len(data)+3, column = 1, sticky = tk.W, padx = 15, pady = 5)
        entry_updateApointmentStatusID.grid(columnspan = 7,row = len(data)+3, column = 1, sticky = tk.N, padx = 15, pady = 5)
        label_ajustment.grid(columnspan = 7,row = len(data), column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_updatedStatus.grid(columnspan = 7,row = len(data)+4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        optionMenu_updateStatus.grid(columnspan = 7,row = len(data)+4, column = 1, sticky = tk.N, padx = 15, pady = 5)
        button_back.grid(columnspan = 7,row = len(data)+7, column = 1, sticky = tk.W, padx = 10, pady = 5)
        button_submitAppointment.grid(columnspan = 7,row = len(data)+7, column = 1, sticky = tk.E, padx = 10, pady = 5)

    def submitID(self, appointment_id, status):
        appointmentList = Appointment.viewAppointmentsByStatusPending()
        for appointment in appointmentList:
           if appointment["id"] == appointment_id:
                Appointment.updateAppointmentStatus(appointment_id,status)
                messagebox.showinfo("SUCCESS", "Update Successfully")
                break
        else:
            messagebox.showinfo("FAILED", "Please make you insert correct appointment id (must be pending appointment!")

class NursePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
         #Widget Creation
        label_dentistPage = tk.Label(self, text = "Nurse Page", font = ("Courier",20),fg = "grey")
        label_ajustment = tk.Label(self, text = "                        ")
        label_generateSummary = tk.Label(self, text = "Generate Summary: ", font = ("Courier",18),fg = "black")
        # button_viewAllAppointment = tk.Button(self, text = "View All Appointment", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(ViewAllAppointmentPageNurse))
        button_overwriteAppointmentStatus = tk.Button(self, text = "Overwrite Appointment Status", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(OverwriteAppointmentStatus))
        button_generateSummaryByName = tk.Button(self, text = "By Customer's Name", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByName))
        button_generateSummaryByIC = tk.Button(self, text = "By Customer's NRIC", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByIC))
        button_generateSummaryByTreatment = tk.Button(self, text = "By Treatment Type", font = ("Courier",18), fg = "black", height = 2, width = 40, command = lambda: master.switch_frame(GenerateSummaryByTreatment))
        button_logout = tk.Button(self, text = "Logout", font = ("Courier",15), fg = "grey", height = 2, width = 7, command = lambda: master.switch_frame(MainPage))
        #widget Positioning
        label_ajustment.grid(row = 0, column = 0)
        label_dentistPage.grid(row = 0, column = 1, sticky = tk.W, padx = 10, pady = 10)
        # button_viewAllAppointment.grid(row = 2, column = 1, sticky = tk.W, padx = 10, pady = 10)
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
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8, command = lambda: self.submitID(entry_customerName.get()))
        label_ajustment = tk.Label(self, text = "")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        #Widget Positioning
        label_ajustment.grid(columnspan = 8, row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByName.grid(columnspan = 8, row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByNameInfo.grid(columnspan = 8, row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_customerName.grid(columnspan = 8, row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        button_submit.grid(columnspan = 8, row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)
        button_back.grid(columnspan = 8, row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)
    
    def submitID(self,  customer_name):
        appointmentList = State.getAppointmentList()
        for appointment in appointmentList:
           if appointment.customer_name == customer_name:
                self.showDetails(customer_name)
                break
        else:
            messagebox.showinfo("FAILED", "Please make you insert correct customer name!")

    def showDetails(self, customer_name):
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.generateAppointmentSummaryByCustomerName(customer_name))
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+6, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1
    
    
        
class GenerateSummaryByIC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Widget Creation
        label_generateSummaryByIC = tk.Label(self, text = "Generate Summary By NRIC", font = ("Courier",20),fg = "grey")
        label_generateSummaryByICInfo = tk.Label(self, text = "Please enter NRIC number that you wish to search: ",font = ("Courier",15),fg = "black" )
        entry_customerIC = tk.Entry(self)   
        button_submit = tk.Button(self, text = "Sumbit", font = ("Courier",15), fg = "black", height = 1, width = 8, command = lambda: self.submitNRIC(entry_customerIC.get()))
        label_ajustment = tk.Label(self, text = "")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        #Widget Positioning
        label_ajustment.grid(columnspan = 8, row = 0, column = 0, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByIC.grid(columnspan = 8, row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        label_generateSummaryByICInfo.grid(columnspan = 8, row = 1, column = 1, sticky = tk.W, padx = 15, pady = 5 )
        entry_customerIC.grid(columnspan = 8, row = 2, column = 1, sticky = tk.S, padx = 15, pady = 5)
        button_submit.grid(columnspan = 8, row = 2, column = 1, sticky = tk.E, padx = 15, pady = 5)
        button_back.grid(columnspan = 8, row = 4, column = 1, sticky = tk.W, padx = 15, pady = 5)

    def submitNRIC(self,  customer_nric):
        appointmentList = State.getAppointmentList()
        for appointment in appointmentList:
           if appointment.customer_nric == customer_nric:
                self.showDetails(customer_nric)
                break
        else:
            messagebox.showinfo("FAILED", "Please make you insert correct customer name!")

    def showDetails(self, customer_nric):
        data = [
            {
                "id": "Appointment ID",
                "date": "Date",
                "timeslot_time": "Time Slot",
                "customer_name": "Customer Name",
                "customer_nric" : "NRIC",
                "dentist": "Dentist",
                "treatment": "Treatment",
                "status": "Status",
            }
        ]
        data.extend(Appointment.generateAppointmentSummaryByCustomerNRIC(customer_nric))
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                if j == "id" or j == "date" or j == "timeslot_time" or j == "customer_name" or j == "customer_nric" or j == "dentist" or j == "treatment" or j == "status":
                    self.e.grid(row=i+6, column=k, sticky = tk.N)
                    self.e.insert(tk.INSERT, data[i][j])
                    self.e.configure(state="readonly")
                k+=1

class GenerateSummaryByTreatment(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        data = [
            {
                "typeOfTreatment": "Type of Treatment",
                "customerCount": "Total Customers count"
            }
        ]
        data.extend(Appointment.viewTotalCustomersByTypes())
        for i in range(len(data)):
            k = 0
            for j in data[0]:
                if i == 0:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11, "bold"))
                else:
                    self.e = Entry(self, width=15, fg="black", font=("Courier", 11))
                self.e.grid(row=i+1, column=k, sticky = tk.W)
                self.e.insert(tk.INSERT, data[i][j])
                self.e.configure(state="readonly")
                k+=1

        # #Widget Creation
        label_generateSummaryByTreatment = tk.Label(self, text = "Generate Summary By Treatment Type", font = ("Courier",20),fg = "grey")
        button_back = tk.Button(self, text = "Back", font = ("Courier",15), fg = "grey", height = 2, width = 6, command = lambda: master.switch_frame(NursePage))       
        # #Widget Positioning
        label_generateSummaryByTreatment.grid(row = 0, column = 1, sticky = tk.W, padx = 15, pady = 5)
        button_back.grid(row = len(data)+4, column = 1, sticky = tk.W, padx = 15, pady = 5)
        
def main():
    app = DentistApp()
    app.title('Oriental Dentist Clinic')
    app.geometry("670x530")
    app.mainloop()