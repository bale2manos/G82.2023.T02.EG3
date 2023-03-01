"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime

class OrderRequest:
    """Class representing the register of the patient in the system"""
    def __init__( self, product_id, order_type, delivery_address, phone_number, zip_code ):
        self.__product_id = product_id
        self.__delivery_address = delivery_address
        self.__order_type = order_type
        self.__phone_number = phone_number
        self.__zip_code = zip_code
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def full_name( self ):
        """Property representing the name and the surname of
        the person who request the registration"""
        return self.__delivery_address

    @full_name.setter
    def full_name( self, value ):
        self.__delivery_address = value

    @property
    def vaccine_type( self ):
        """Property representing the type vaccine"""
        return self.__order_type
    @vaccine_type.setter
    def vaccine_type( self, value ):
        self.__order_type = value

    @property
    def phone_number( self ):
        """Property representing the requester's phone number"""
        return self.__phone_number
    @phone_number.setter
    def phone_number( self, value ):
        self.__phone_number = value

    @property
    def patient_id( self ):
        """Property representing the requester's UUID"""
        return self.__product_id
    @patient_id.setter
    def patient_id( self, value ):
        self.__product_id = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def patient_system_id( self ):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()

    @property
    def patient_age( self ):
        """Returns the patient's zip_code"""
        return self.__zip_code