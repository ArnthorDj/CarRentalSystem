class Person():
    def __init__(self, ssn, name):
        self.__ssn = ssn
        self.__name = name
    
    def getSsn(self):
        return self.__ssn
    def getName(self):
        return self.__name
    
    def setSsn(self, new_ssn):
        self.__ssn = new_ssn
    def setName(self, new_name):
        self.__name = new_name

    def __str__(self):
        return "{:<15}{}\n{:<15}{}".format("Kennitala:", self.getSsn(), 
                                           "Nafn:", self.getName())
    def __repr__(self):
        return "{},{}".format(self.getSsn(), self.getName())