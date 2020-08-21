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
                status = "Complated",
                user_id = 4                 
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Fillings",
                date = 20200823,
                timeslot = 3,
                status = "Pending",
                user_id = 4   
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Kah Wei",
                customer_nric = "960411075647",
                dentist = "Dr. Stanley",
                treatment = "Extractions",
                date = 20200820,
                timeslot = 2,
                status = "No-show",
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
                status = "Completed",
                user_id = 5
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Teeth Cleaning",
                date = 20200824,
                timeslot = 4,
                status = "Pending",
                user_id = 5
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Lee Min Er",
                customer_nric = "9604155689",
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200823,
                timeslot = 7,
                status = "Comfirmed",
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
                date = 20200825,
                timeslot = 13,
                status = "Confirmed",
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
                dentist = "Dr. Stanley",
                treatment = "Denture",
                date = 20200806,
                timeslot = 13,
                status = "Rejected",
                user_id = 6
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Koay Evon",
                customer_nric = "956321458523",
                dentist = "Dr. Ong",
                treatment = "Teeth Cleaning",
                date = 20200806,
                timeslot = 6,
                status = "Completed",
                user_id = 7
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Koay Evon",
                customer_nric = "956321458523",
                dentist = "Dr. Stanley",
                treatment = "Teeth Cleaning",
                date = 20200822,
                timeslot = 6,
                status = "Pending",
                user_id = 7
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Low Lee Yee",
                customer_nric = "95632555562",
                dentist = "Dr. Ong",
                treatment = "Fillings",
                date = 20200822,
                timeslot = 8,
                status = "Pending",
                user_id = 8
            )
        )

        State.addAppointment(
            Appointment (
                customer_name = "Low Lee Yee",
                customer_nric = "95632555562",
                dentist = "Dr. Ong",
                treatment = "Repairs",
                date = 20200806,
                timeslot = 8,
                status = "Completed",
                user_id = 8
            )
        )

        


        



