"""class for testing the regsiter_order method"""
import unittest
import os
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time
from pathlib import Path


class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    __order_request_json_store = None

    @classmethod
    def setUpClass(cls) -> None:
        """setup class"""
        store_path = "../../main/python/stores/"
        current_path = os.path.dirname(__file__)
        cls.__order_request_json_store = os.path.join(current_path, store_path, "order_requests.json")

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @freeze_time("2023-03-08")
    def test_something( self ):
        """dummy test"""
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual(True, False)

    @freeze_time("2023-03-08")
    def test_product_id_invalid_str( self ):
        """dummy test"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalide EAN13 string", cm.exception.message)

    @freeze_time("2023-03-08")
    def test_json_file(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/DSoftware/G82.2023.T02.EG3/src/python/stores"
        file_store = JSON_FILES_PATH + "order_product.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


if __name__ == '__main__':
    unittest.main()
