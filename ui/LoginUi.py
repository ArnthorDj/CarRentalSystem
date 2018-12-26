from service.LoginService import LoginService
class LoginUi():
    def __init__(self):
        self.__login_service = LoginService()
    
    def loginMenu(self):
        login = True
        print("---Innskráning---")
        while login:
            number = self.getInputs(1, "Númer:", "\tNúmer þarf að vera tölustafur.")
            #number = input("{:<15}".format("Númer:"))
            password = self.getInputs(2, "Lykilorð:", "\tLykilorð þarf að innihalda 1 stóran staf 2 tölustafi\n\tog vera a.m.k. 6 stafi af lengd.")
            #password = input("{:<15}".format("Lykilorð:"))
            
            login = not self.__login_service.Login()
        print("-----------------")
    
    def getInputs(self, number, input_rext, error_message):
        right_input = True
        user_input = input("{:<15}".format(input_rext))
        while right_input:
            if(number == 1):
                right_input = not self.__login_service.checkNumber(user_input)
            elif(number == 2):
                right_input = not self.__login_service.checkPassword(user_input)
            
            if(right_input):

                print(error_message)
                user_input = input("{:<15}".format(input_rext))

        return user_input