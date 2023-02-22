"""Module """
from .order_management_exception import OrderManagementException
class OrderManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13, OR FALSE IN OTHER CASE"""
        return True

    def register_order (self, product_id, order_type, address, phone_number, zip_code):
        """Crear un pedido con la información necesaria"""
        # un metodo para validar cada input
        if not self.validate_product_id(product_id):
            raise OrderManagementException("Wrong product ID")
        raise OrderManagementException("Not implemented yet")
    
    def validate_product_id(self, product_id):
        raise OrderManagementException("Not implemented yet")

    