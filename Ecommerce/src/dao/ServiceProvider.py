# ServiceProvider class in Ecommerce/src/ServiceProvider.py

from Ecommerce.src.exception import CustomerNotFoundException

class ServiceProvider:
    def __init__(self, db_util):
        self.db_util = db_util

    def fetch_customer_by_id(self, customer_id):
        # Implement logic to fetch a customer by ID from the database
        # For example, assuming you have a 'customers' table:
        conn = self.db_util.getconn()
        try:
            with conn.cursor() as cursor:
                select_query = "SELECT * FROM customers WHERE cust_id = %s"
                cursor.execute(select_query, (customer_id,))
                customer_data = cursor.fetchone()

                if customer_data:
                    # Assuming you have a Customer class to represent customer data
                    cust_id, name, email, password = customer_data
                    return Customer(cust_id, name, email, password)
                else:
                    # If no customer found, raise CustomerNotFoundException
                    raise CustomerNotFoundException(f"Customer not found with ID {customer_id}")
        finally:
            conn.close()

    # Other methods...

# Your Customer class (assuming you have one)
class Customer:
    def __init__(self, cust_id, name, email, password):
        self.cust_id = cust_id
        self.name = name
        self.email = email
        self.password = password

