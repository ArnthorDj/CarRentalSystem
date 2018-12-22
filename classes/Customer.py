from models.Person import Person
class Customer(Person):
    def __init__(self, name, ssn, home_address, phone_number, country, creditcard_id={}):
        Person.__init__(self, name, ssn)
        self.__home_address = home_address
        self.__phone_number = phone_number
        self.__country = country
        self.__creditcard_id = creditcard_id

    def getAddress(self):
        return self.__home_address
    def getPhone(self):
        return self.__phone_number
    def getCountry(self):
        return self.__countryss
    def getCreditcard_id(self):
        return self.__creditcard_id

    def setAddress(self, new_home_address):
        self.__home_address = new_home_address
    def setPhone(self, new_phone_number):
        self.__phone_number = new_phone_number
    def setCountry(self, new_country):
        self.__country = new_country
    
    def addCreditCard(self, new_cred):
        if(new_cred in self.__creditcard_id):
            return "Kretid kortið er nú þegar skráð á Viðskiptavin."
        self.__creditcard_id[new_cred.getCreditCardNumber()] = new_cred
        return "Kretid kort hefur verið bætt við hjá viðskiptavini."
    def removeCreditCard(self, del_cred):
        if(new_cred in self.__creditcard_id):
            del self.__creditcard_id[del_cred]
            return "Kretid kort hefur verið eytt af viðskiptavini."
        return "Kretid kort er ekki skráð á viðskiptavin."
    def __str__(self):
        return "{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}".format("Kennitala:", 
                                                                         self.getSsn(),
                                                                         "Nafn:", self.getName(),
                                                                         "Heimilisfang:", self.getAddress(),
                                                                         "Símanúmer:", self.getPhone(),
                                                                         "Land:", self.getCountry())
    def __repr__(self):
        return "{},{},{},{},{}".format(self.getSsn(), self.getName(),
                                       self.getAddress(), self.getPhone(),
                                       self.getCountry())