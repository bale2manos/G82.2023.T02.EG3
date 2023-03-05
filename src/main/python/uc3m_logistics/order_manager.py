"""Module """
import json
import re
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException

class OrderManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass
    @classmethod
    def validate_ean13(cls, ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13, OR FALSE IN OTHER CASE"""
        valid_structure = re.search("^[0-9]{13}$", ean13_code)
        if not valid_structure:
            return False

        digit_counter = 1
        sum_total = 0
        while digit_counter <= 12:
            par_position = digit_counter % 2 == 0
            digit = int(ean13_code[digit_counter - 1])
            if par_position:
                sum_total += digit * 3
            else:
                sum_total += digit
            digit_counter += 1
        mod = sum_total % 10
        check_digit = 10 - mod

        if check_digit == 10:
            check_digit = 0
        if check_digit != int(ean13_code[12]):
            return False

        return True

    # LAS OTRAS 3 FUNCIONES + AUXILIARES(no comporobarlas)
    def register_order (self, product_id: int, order_type: str, address:str,
                        phone_number: int, zip_code: int):
        """FUNCIÓN 1"""
        # validar inputs con funciones auxiliares
        if not self.validate_order_type(order_type):
            raise OrderManagementException("Invalid product id")


        # crear order request object
        order_request = OrderRequest(product_id, order_type, address,
                        phone_number, zip_code)
        # write order request to file
        with open("../stores/order_requests.json", "w", encoding="utf-8") as file:
            data = json.load(file)
            data.append(order_request)
            json.dump(data, file)



        return order_request.order_id()
        raise NotImplementedError("falta por hacer")
    def send_product (self, input_file:str) -> str:
        """FUNCIÓN 2: Devuelve un String en hexadecimal que representa el código de
        seguimiento del envío """
        raise NotImplementedError("falta por hacer")


    def deliver_product(tracking_number:str) -> bool:
        """FUNCIÓN 3: Cuando el pedido llegue a su destino, el sistema registrará que se ha
        entregado al cliente. El sistema comprobará que el código de seguimiento es correcto y
        que el día es el programado (supondremos que sólo se puede entregar en la fecha
        prevista). Finalmente registrará la entrega en un fichero."""
        raise NotImplementedError("falta por hacer")

    @classmethod
    def validate_order_type(cls, order_type):
        if not isinstance(order_type, str):
            return False
        return True

