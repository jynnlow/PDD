from app.models.appointment import Appointment
from app.models.customer import Customer
from app.models.dentist import Dentist
from app.state.state import State
from app.models.user import User
from app.sharedkernel.general import General
from datetime import date, timedelta

from pprint import pprint
# Mocks
from mocks.appointment import AppointmentMock
from mocks.user import UserMock
# GUI
import app.view.gui as GUI

def main():
    AppointmentMock.mockAppointments()
    UserMock.mockUsers()
    GUI.main()
    
if __name__ == "__main__":
    main()