from app.models.appointment import Appointment
from app.models.customer import Customer
from app.models.dentist import Dentist
from app.state.state import State
from app.models.user import User
from app.sharedkernel.general import General
from datetime import date
from pprint import pprint
# Mocks
from mocks.appointment import AppointmentMock
from mocks.user import UserMock

def main():
    AppointmentMock.mockAppointments()
    print(Appointment.createAppointment(20200815,3))
    # Mock.mockUsers()
    # Mock.mockAppointments()
    # today = date.today()
    # changeFormat = today.strftime("%Y%m%d")
    # print("Today is", today)
    # print(changeFormat)
    # pprint(Appointment.getAppointmentSlotOptions())
    
if __name__ == "__main__":
    main()