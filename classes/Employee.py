from classes.Person import Person
class Employee(Person):
    def __init__(self, name, ssn, employee_id, password, position):
        Person.__init__(self, name, ssn)
        self.__id = employee_id
        self.__password = password
        self.__position = position
    
    def getId(self):
        return self.__id
    def getPassword(self):
        return self.__password
    def getPosition(self):
        return self.__position
    def getPositionText(self):
        num = self.getPosition()
        if(numb == 0):
            return "Venjulegur"
        elif(num == 1):
            return "Admin"
        elif(num == 2):
            return "Stjóri"
        else:
            return "Villa"

    def setId(self, new_id):
        self.__id = new_id
    def setPassword(self, password):
        self.__password = password
    def setPosition(self, new_position):
        self.__position = new_position
    
    def __str__(self):
        return "{:<15}{}\n{:<15}{}\n{:<15}{}".format("Starfsmans Númer:", self.getId(),
                                                     "Kennitala:", self.getSsn(),
                                                     "Nafn:", self.getName()
                                                     "Staða:", self.getPositionText())
    def __repr__(self):
        return "{},{},{},{}".format(self.getId(), self.getSsn(), self.getName(), self.getPassword())