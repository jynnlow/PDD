from app.state.state import State
from app.models.appointment import Appointment

class AppointmentMock:
    def mockAppointments():
        State.addAppointment(
            Appointment (
                id = "A0001",
                user_id = 100,
                cancel = False,
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Ong",
                treatment = "Fillings",
                date = 20200815,
                timeslot = 1,
                remark = "",
                status = "Pending"                 
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0002",
                user_id = 100,
                cancel = False,
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Fillings",
                date = 20200813,
                timeslot = 3,
                remark = "",
                status = "Completed"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0003",
                user_id = 100,
                cancel = False,
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Extraction",
                date = 20200816,
                timeslot = 2,
                remark = "",
                status = "Pending"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0004",
                user_id = 101,
                cancel = False,
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Extraction",
                date = 20200815,
                timeslot = 10,
                remark = "",
                status = "Confirmed"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0005",
                user_id = 101,
                cancel = False,
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Teeth Cleaning",
                date = 20200813,
                timeslot = 4,
                remark = "",
                status = "No-show"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0006",
                user_id = 101,
                cancel = False,
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200817,
                timeslot = 7,
                remark = "",
                status = "Pending"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0007",
                user_id = 102,
                cancel = False,
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200815,
                timeslot = 8,
                remark = "",
                status = "Pending"   
            )
        )

        State.addAppointment(
            Appointment (
                id = "A0008",
                user_id = 102,
                cancel = False,
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Ong",
                treatment = "repairs",
                date = 20200814,
                timeslot = 13,
                remark = "",
                status = "Completed"   
            )
        )



