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
    def test_CE_V_1_2_4_9_10(self):
        """All parameters okay, check output"""
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        #hex_pattern = "0[xX][0-9a-fA-F]+"
        self.assertEqual(value, "944f15e32a64345933979293a7244fa9")
        #self.assertTrue(re.search(hex_pattern, value))

    @freeze_time("2023-03-08")
    def test_CE_V_5(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual(value, "99a5c8ff0f471baca42ca20ddac530c7" )

    @freeze_time("2023-03-08")
    def test_CE_V_6(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",	"CALLE EJEMPLOPRUEBA",
                                        "+34123456789", 28005)
        self.assertEqual(value, "39aa8497dc4bb47c2b686d33f7260250")

    @freeze_time("2023-03-08")
    def test_CE_V_7(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR",	"CALLE EJEMPLODECALLEPARAHACERLAPRUEBAEJEMPLOPARAHACERLAPRUEBAEJEMPLOPARAHACERLAPRUEBAEJEMPLOPARAHAC",
                                        "+34123456789", 28005)
        self.assertEqual(value, "7abd2c1a7670c00af61752679cf27882")

    @freeze_time("2023-03-08")
    def test_CE_V_8(self):
        my_order = OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "CALLE EJEMPLOPARAHACERPRUEBASEJEMPLOPARAHACERPRUEBASEJEMPLOPARAHACERPRUEBASEJEMPLOPARAHACERPRUEBASEJ",
                                        "+34123456789", 28005)
        self.assertEqual(value, "385af0b83ecd8ba8816af3248e091844")


    @freeze_time("2023-03-08")
    def test_CE_NV_1(self):
        """Product ID not a number"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("842169142322A", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid product id", cm.exception.message)

    @freeze_time("2023-03-08")
    def test_CE_NV_2(self):
        """Product ID not an EAN13"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423225", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid product id", cm.exception.message)


    @freeze_time("2023-03-08")
    def test_CE_NV_3(self):
        """Order Type other str"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "POTATO",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid order type", cm.exception.message)


    @freeze_time("2023-03-08")
    def test_CE_NV_4(self):
        """Order Type not a str"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", 123,	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid order type", cm.exception.message)

    def test_CE_NV_5(self):
        """Address not a str"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"3435445 7890",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid address", cm.exception.message)


    def test_CE_NV_6(self):
        """Address less than minimum chars(19)"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"C/PO,4, PATA, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid address", cm.exception.message)

    def test_CE_NV_7(self):
        """Address over maximum chars(101)"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"C/ EJEMPLO PARA DIRECCION CON EL NUMERO DE CARACTERES POR DEBAJO JUSTO DEL NUMERON, 14, MADRID, SPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid address", cm.exception.message)

    def test_CE_NV_8(self):
        """Address does not have a space"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"CALLEPO4PATASPAIN",
                                        "+34123456789", 28005)
        self.assertEqual("Invalid address", cm.exception.message)

    def test_CE_NV_9(self):
        """Phone less than minimum digits(11)"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+34123456", 28005)
        self.assertEqual("Invalid phone number", cm.exception.message)


    def test_CE_NV_10(self):
        """Phone over maximum digits(14)"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "+3412345679777", 28005)
        self.assertEqual("Invalid phone number", cm.exception.message)

    def test_CE_NV_12(self):
        """Phone without + at the beggining"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR",	"C/LISBOA,4, MADRID, SPAIN",
                                        "34123456789", 28005)
        self.assertEqual("Invalid phone number", cm.exception.message)

    @freeze_time("2023-03-08")
    def test_CE_NV_13(self):
        """Phone number not a str"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                    34123456789, 28005)
        self.assertEqual("Invalid phone number", cm.exception.message)

    @freeze_time("2023-03-08")
    def test_CE_NV_15(self):
        """Zip Code not valid"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                            "+34123456789", 618005)
        self.assertEqual("Invalid zip code", cm.exception.message)

    @freeze_time("2023-03-08")
    def test_CE_NV_16(self):
        """Order id not correct"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                            "+34123456789", 618005)
        self.assertEqual(value, "lo q tenga q salir")

    @freeze_time("2023-03-08")
    def test_CE_NV_17(self):
        """File does not exist"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/DSoftware/G82.2023.T02.EG3/src/python/stores"
        file_store = JSON_FILES_PATH + "order_product.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN",
                                            "+34123456789", 28005)
        self.assertEqual("File not found", cm.exception.message)


    def test_CE_NV_18(self):
        """Error al decodificar el JSON""" # TODO no se como hacer
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/DSoftware/G82.2023.T02.EG3/src/python/stores"
        file_store = JSON_FILES_PATH + "order_product.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        raise NotImplementedError("No implementado")

    @freeze_time("2023-03-08")
    def test_json_file(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/DSoftware/G82.2023.T02.EG3/src/python/stores"
        file_store = JSON_FILES_PATH + "order_product.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


if __name__ == '__main__':
    unittest.main()
