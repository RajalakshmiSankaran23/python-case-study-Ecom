from Ecommerce.src.Entity.Model.Customer import Customer
from Ecommerce.src.Entity.Model.Product import Product
from Ecommerce.src.util.DButil import DBUtil
from Ecommerce.src.exception import EcommerceException
from Ecommerce.src.dao.ServiceProvider import ServiceProvider


db_util = DBUtil()
conn = db_util.getconn()

class ServiceProviderImpl(ServiceProvider):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def add_product(self, product):
        try:

            connection = DBConnUtil.get_connection(self.connection_string)


        except Exception as e:
            raise EcommerceException(f"Error adding product: {str(e)}")

    def get_user_by_id(self, user_id):
        try:

            connection = DBConnUtil.get_connection(self.connection_string)


        except Exception as e:
            raise EcommerceException(f"Error retrieving user: {str(e)}")
