"""Contains the class OrderShipping"""
from datetime import datetime
import hashlib

class OrderShipping():
    """Class representing an appoinment  for the vaccination of a patient"""

    def __init__( self, product_id, order_id, delivery_phone_number, order_type ):
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__product_id = product_id
        self.__order_id = order_id
        self.__delivery_phone_number = delivery_phone_number
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        if order_type == "Regular":
            delivery_days = 7
        else:
            delivery_days = 1

        #timestamp is represneted in seconds.microseconds
        #zip_code must be expressed in senconds to be added to the timestap
        self.__delivery_day = self.__issued_at + (delivery_days * 24 * 60 * 60)

    def __signature_string(self):
        """Composes the string to be used for generating the key for the date"""
        return "{alg:" + self.__alg +",typ:" + self.__type +",order_id:" + self.__order_id + ",issuedate:" + self.__issued_at + ",deliveryday:" + self.__delivery_day + "}"

    @property
    def product_id( self ):
        """Property that represents the product_id of the patient"""
        return self.__product_id

    @product_id.setter
    def product_id( self, value ):
        self.__product_id = value

    @property
    def order_id( self ):
        """Property that represents the order_id of the patient"""
        return self.__order_id
    @order_id.setter
    def order_id( self, value ):
        self.__order_id = value

    @property
    def phone_number( self ):
        """Property that represents the phone number of the patient"""
        return self.__delivery_phone_number

    @phone_number.setter
    def phone_number( self, value ):
        self.__delivery_phone_number = value

    @property
    def vaccination_signature( self ):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at( self, value ):
        self.__issued_at = value

    @property
    def delivery_day( self ):
        """Returns the vaccination date"""
        return self.__delivery_day