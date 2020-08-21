from app.state.state import State
from app.models.dentist import Dentist
from app.models.customer import Customer
from app.models.nurse import Nurse

class UserMock:
    def mockUsers():
        State.addUser(
            Dentist(
                id = 1,
                username = "stanley001",
                password = "001001001",
                fullName = "Dr.Stanley",
                nric = "990203075164",
                gender = "Male",
                contactNumber = "0125822587",
                address = "26, Jalan Cantil, 16599,Penang, Malaysia"
            )
        )

        State.addUser(
            Dentist(
                id = 2,
                username = "ong002",
                password = "002002002",
                fullName = "Dr.Ong",
                nric = "893193891378",
                gender = "Male",
                contactNumber = "0164822695",
                address = "2, Lorong Teratai Indah, 13400,Penang, Malaysia"
            )
        )

        State.addUser(
            Nurse(
                id = 3,
                username = "nurse003",
                password = "003003003",
                fullName = "Ms.Nurse",
                nric = "850123856584",
                gender = "Female",
                contactNumber = "01265876436",
                address = "13, Taman Kheng Tian, 13400,Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 4,
                username = "leekahwei100",
                password = "100100100",
                fullName = "Lee Kah Wei",
                nric = "960411075647",
                gender = "Male",
                contactNumber = "0124912446",
                address = "50-6-10, Taman Sri Hijau, Jalan Van Praagh, 11600, Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 5,
                username = "leeminer101",
                password = "101101101",
                fullName = "Lee Min Er",
                nric = "9604155689",
                gender = "Female",
                contactNumber = "0121235877",
                address = "49, Taman Cantik, Jalan Cantik, 15622, Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 6,
                username = "tanyunching102",
                password = "102102102",
                fullName = "Tan Yun Ching",
                nric = "964123589646",
                gender = "Female",
                contactNumber = "0124555896",
                address = "49, Taman Pondok, Jalan Yes, 45622, Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 7,
                username = "evonkoay103",
                password = "103103103",
                fullName = "Koay Evon",
                nric = "956321458523",
                gender = "Female",
                contactNumber = "0169852364",
                address = "9, Taman Hjiau 4, Jalan Tomato, 45996, Penang, Malaysia"
            )
        )

        State.addUser(
            Customer(
                id = 8,
                username = "leeyee104",
                password = "104104104",
                fullName = "Low Lee Yee",
                nric = "95632555562",
                gender = "Male",
                contactNumber = "0124545926",
                address = "282, Taman Padini, 45622, Penang, Malaysia"
            )
        )




        
        
        