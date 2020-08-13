from app.models.customer import Customer
from app.models.dentist import Dentist
from app.state.state import State
from app.state.mock import Mock

def main():
    Mock.mockUsers()
    for user in State.getUserList():
        print(user.role)

if __name__ == "__main__":
    main()