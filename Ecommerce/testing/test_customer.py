import unittest
from Ecommerce.src.Entity.Model.Customer import Customer
from Ecommerce.src.Entity.Model.Product import Product



class TestEcommerce(unittest.TestCase):

    def test_product_creation(self):
        prod = Product(product_id=401, name='Pendrive', price=500)
        result = self.opr_instance.create_product(product=prod)
        self.assertEqual(result, True, 'Product Creation Successful.')

    def test_customer_reg(self):
        cust = Customer(customer_id=101, name='ramya', email='ramya@gmail.com', password='ramya123')
        result = self.opr_instance.create_customer(customer_object=cust)
        self.assertEqual(result, True, 'Customer Registration Successful.')



if __name__ == '_main_':
    unittest.main()
