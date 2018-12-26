from database.EmployeeDatabase import EmployeeDatabase
class LoginService():
    def __init__(self):
        self.__employee_database = EmployeeDatabase()
    
    def checkNumber(self, number):
        return number.isdigit()
    def checkPassword(self, password):
        upper_case = 0
        digit = 0
        for letter in password:
            if(letter.isupper()):
                upper_case += 1
            elif(letter.isdigit()):
                digit += 1
        return len(password) >= 6 and digit >= 2 and upper_case >= 1