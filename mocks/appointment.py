from app.state.state import State
from app.models.appointment import Appointment

class AppointmentMock:
    def mockAppointments():
        State.addAppointment(
            Appointment (
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Ong",
                treatment = "Fillings",
                date = 20200815,
                timeslot = 1,
                status = "Pending",
                user_id = 4                 
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Fillings",
                date = 20200813,
                timeslot = 3,
                status = "Completed",
                user_id = 4   
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Extractions",
                date = 20200816,
                timeslot = 2,
                status = "Pending",
                user_id = 4   
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Extractions",
                date = 20200815,
                timeslot = 10,
                status = "Confirmed",
                user_id = 5
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Teeth Cleaning",
                date = 20200813,
                timeslot = 4,
                status = "No-show",
                user_id = 5
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200817,
                timeslot = 7,
                status = "Pending",
                user_id = 5
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200815,
                timeslot = 8,
                status = "Pending",
                user_id = 6
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Ong",
                treatment = "Repairs",
                date = 20200814,
                timeslot = 13,
                status = "Completed",
                user_id = 6
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Ong",
                treatment = "Repairs",
                date = 20200823,
                timeslot = 13,
                status = "Pending",
                user_id = 6
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Tan Yun Ching",
                customer_nric = "964123589646",
                dentist = "Dr. Ong",
                treatment = "Denture",
                date = 20200823,
                timeslot = 13,
                status = "Pending",
                user_id = 6
            )
        )



