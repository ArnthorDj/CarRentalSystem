class Orders():
    def __init__(self, order_id, car_plate_number, customer_ssn, employee_number, pick_up_date, return_date, car_cost, insurance_cost, payment, paid):
        self.__order_id = order_id
        self.__car_plate_number = car_plate_number
        self.__customer_ssn = customer_ssn
        self.__employee_number = employee_number
        self.__pick_up_date = pick_up_date
        self.__return_date = return_date
        self.__days = self.__return_date - self.__pick_up_date
        self.__car_cost = car_cost
        self.__insurance_cost = insurance_cost
        self.__payment = payment
        self.__paid = paid
    
    def getOrderId(self):
        return self.__order_id
    def getCarPlateNumber(self):
        return self.__car_plate_number
    def getCar():
        return
    def getCustomerSsn(self):
        return self.__customer_ssn
    def getEmployeeNumber(self):
        return self.__employee_number
    def getPickUpDate(self):
        return self.__pick_up_date
    def getReturnDate(self):
        return self.__return_date
    def getInsurenceCost(self):
        return self.__insurance_cost
    def getPayment(self):
        return self.__payment
    def getPaid(self):
        return self.__paid
    
    def setOrderId(self, new_order_id):
        self.__order_id = new_order_id
    def setCarPlateNumber(self, new_car_plate_number):
        self.__car_plate_number = new_car_plate_number
    def setCustomerSsn(self, new_customer_ssn):
        self.__customer_ssn = new_customer_ssn
    def setEmployeeNumber(self, new_employee_number):
        self.__employee_number = new_employee_number
    def setPickUpDate(self, new_pick_up_date):
        self.__pick_up_date = new_pick_up_date
    def setReturnDate(self, new_return_date):
        self.__return_date = new_return_date
    def setInsurenceCost(self, new_insurence_cost):
        self.__insurance_cost = new_insurence_cost
    def setPayment(self, new_payment):
        self.__payment = new_payment
    def setPaid(self, new_paid):
        self.__paid = new_paid
    def __str__(self):
        return "{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}".format(
            "Pöntunar Númer:", self.__order_id, "Númera Plata:", self.__car_plate_number, "Kennitala:", self.__customer_ssn, "Númer Starfsmans", self.__employee_number,
            "Skæja Dagsetning:", self.__pick_up_date, "Skila Dagsetning", self.__return_date, "Fjöldi Daga:", self.__days, "Tryggingar:", self.__insurance_cost,
            "Kosnaður:", self.__payment, "Borgað:", self.__paid)
    def __repr__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.__order_id, self.__car_plate_number, self.__customer_ssn, self.__employee_number, self.__pick_up_date,
                                                      self.__return_date, self.__days, self.__insurance_cost, self.__payment, self.__paid)