from app.models.customer import Customer
from app.models.dentist import Dentist
from app.state.state import State
from app.state.mock import Mock
from app.models.user import User

def main():
    Mock.mockUsers()
    # for user in State.getUserList():
    #     print(user.role)
    
    username = "jynnlow99"
    password = "04110203"
    returnMessage = User.logout()
    print(returnMessage)
    

if __name__ == "__main__":
    main()