from Ecommerce.src.Entity.Model.Customer import Customer
from Ecommerce.src.Entity.Model.Product import Product
from Ecommerce.src.util.DButil import DBUtil
from Ecommerce.src.Entity.Model.Cart import Cart

class MainModule:

    def display_menu(self):
        print("\n  ECOMMERCE SYSTEM  ")
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Cart management")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.customer_management()
            elif choice == '2':
                self.product_management()
            elif choice == '3':
                self.cart_management()
            elif choice == '4':
                print("Exiting the E-Commerce System. Goodbye!")
                break
            else:
                print("Invalid choice.")

    def customer_management(self):
        print("1. Add New Customer")
        print("2. Update Customer Information")
        print("3. Retrieve Customer Information")
        print("4. Exit")

        while True:
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_new_customer()
            elif choice == '2':
                self.update_customer_information()
            elif choice == '3':
                self.retrieve_customer_information()
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_customer(self):
        try:
            cust_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")

            new_customer = Customer(cust_id, name, email, password)
            db_util = DBUtil()
            new_customer.insert_customer(db_util)

        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

    def update_customer_information(self):
        try:
            cust_id = int(input("Enter customer ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            db_util = DBUtil()
            customer = Customer(cust_id, '', '', '')
            customer.update_customer_information(db_util, cust_id, new_name, new_email, new_password)
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")
   


    def retrieve_customer_information(self):
        try:
            cust_id = int(input("Enter customer ID to retrieve information: "))
            db_util = DBUtil()
            customer = Customer(cust_id, '', '', '')
            customer.retrieve_customer_information(db_util, cust_id)
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

    def product_management(self):
        print("\n===== Product Management =====")
        print("1. Add new product")
        print("2. Update product")
        print("3. Retrieve product information")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.add_new_products()
        elif choice == '2':
            self.update_product_information()
        elif choice == '3':
            self.retrieve_product_information()
        else:
            print("Invalid choice. Returning to the main menu.")

    def add_new_products(self):
        try:
            product_id = input("Enter product id: ")
            name = input("Enter product name: ")
            price = input("Enter price: ")

            new_product = Product(product_id, name, price)
            db_util = DBUtil()
            new_product.insert_product(db_util)

        except ValueError:
            print("Invalid input.")


    def update_product_information(self):
        try:
            product_id = input("Enter product ID to update: ")
            new_name = input("Enter new name: ")
            new_price = input("Enter new price: ")
            db_util = DBUtil()
            product = Product(product_id, '', '')
            product.update_product_information(db_util, product_id, new_name, new_price)
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")

    def retrieve_product_information(self):
        try:
            product_id = int(input("Enter product ID to retrieve information: "))
            db_util = DBUtil()
            product = Product(product_id, '', '')
            product.retrieve_product_information(db_util, product_id)
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")


    def cart_management(self):
        print("1. Add New Customer")
        #print("2. Update Customer Information")
        #print("3. Retrieve Customer Information")
        print("2. Exit")

        while True:
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_new_cart()
            elif choice == '2':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_cart(self):
        try:
            cart_id=int(input("Enter cart id"))
            cust_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product id: "))
            quantity=int(input("Enter quantity "))

            new_cart = Cart(cart_id,cust_id,product_id,quantity)
            db_util = DBUtil()
            new_cart.insert_cart(db_util)

        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

    def update_cart_information(self):
        try:
            cart_id = int(input("Enter cart ID to update: "))
            new_cust_id = input("Enter new cust_id: ")
            new_product_id = input("Enter new product_id: ")
            new_quantity = input("Enter new quantity: ")
            db_util = DBUtil()
            cart = Cart(cart_id, '', '', '')
            cart.update_cart_information(db_util, cart_id,new_cust_id,new_product_id,new_quantity)
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")



if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
