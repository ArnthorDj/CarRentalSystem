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
        return "Kennitala:\t{}\nNafn:\t{}".format(self.__ssn, self.__name)
    def __repr__(self):
        return "{},{}".format(self.__ssn, self.__name)