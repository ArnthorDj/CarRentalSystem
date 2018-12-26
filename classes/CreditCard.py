class CreditCard():
    customer_ssn,credit_card_number,expiration_date,cvc
    def __init__(self, customer_ssn, credit_card_number, expiration_date, cvc):
        self.__customer_ssn = customer_ssn
        self.__credit_card_number = credit_card_number
        self.__expiration_date = expiration_date
        self.__cvc = cvc
    
    def getCustomerSsn(self):
        return self.__customer_ssn
    def getCreditCardNumber(self):
        return self.__credit_card_number
    def getExpirationDate(self):
        return self.__expiration_date
    def getCvc(self):
        return self.__cvc
    
    def setCustomerSsn(self, new_customer_ssn):
        self.__customer_ssn = new_customer_ssn
    def setCreditCardNumber(self, new_credit_card_number):
        self.__credit_card_number =new_credit_card_number
    def setExpirationDate(self, new_expiration_date):
        self.__expiration_date = new_expiration_date
    def setCvc(self, new_cvc):
        self.__cvc = new_cvc
    
    def __str__(self):
        return "{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}".format(
            "Kennitala:", self.__customer_ssn, "Númer Korts:", self.__credit_card_number,
            "Gildis Tími:", self.__expiration_date, "CVC:", self.__cvc)
    def __repr__(self):
        return "{},{},{},{},{}".format(
            self.__customer_ssn, self.__credit_card_number,
            self.__expiration_date, self.__cvc)