import re
from datetime import date, datetime

class Account:
    def __init__(self, id, username, f_name, surname, email):
        self._id = id
        self._payment_details = PaymentDetails()
        super().__init__()

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        if isinstance(new_basket, Basket) == False:
            raise TypeError('The basket must be an instance of the Basket class')
        else:
            self._basket = new_basket

    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, new_payment_details):
        if isinstance(new_payment_details, PaymentDetails) == False:
            raise TypeError('The payment_details must be an instance of the PaymentDetails class')
        else:
          self._payment_details = new_payment_details