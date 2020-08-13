from app.state.state import State
from app.models.dentist import Dentist
from app.models.customer import Customer

class Mock:
    def mockUsers():
        State.addUser(
            Dentist(
                id = 1,
                username = "leekahwei009",
                password = "1234567890",
                fullName = "Lee Kah Wei",
                nric = "960411075647",
                gender = "Male",
                contactNumber = "0124912446",
                address = "50-6-10, Taman Sri Hijau, Jalan Van Praagh, 11600, Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 2,
                username = "leekahwei009",
                password = "1234567890",
                fullName = "Lee Kah Wei",
                nric = "960411075647",
                gender = "Male",
                contactNumber = "0124912446",
                address = "50-6-10, Taman Sri Hijau, Jalan Van Praagh, 11600, Penang, Malaysia"
            )
        )