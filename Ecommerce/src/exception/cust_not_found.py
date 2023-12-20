# Ecommerce/src/exception/cust_not_found.py

from Ecommerce.src.exception import CustomerNotFoundException, EcommerceException
from Ecommerce.src.dao.ServiceProvider import ServiceProvider  # Assuming this is the correct import

def example_function(customer_id_input):
    try:
        service_provider = ServiceProvider()  # Assuming this is how you create an instance
        customer = ServiceProvider.fetch_customer_by_id(customer_id_input)
        print(f"Customer found: {customer}")
    except CustomerNotFoundException as e:
        print(f"Customer not found: {e}")
    except EcommerceException as e:
        print(f"Ecommerce exception: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    customer_id_input = input("Enter customer ID: ")
    example_function(customer_id_input)
