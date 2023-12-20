from Ecommerce.src.util.DButil import DBUtil

class Cart:
    def __init__(self,cart_id,cust_id,product_id,quantity):
        self.cart_id=cart_id
        self.cust_id=cust_id
        self.product_id=product_id
        self.quantity=quantity

    def insert_cart(self, db_util: DBUtil):
        conn = db_util.getconn()

        create_table_str = '''
         CREATE TABLE IF NOT EXISTS cart (
             cart_id int,
             cust_id int,
             product_id int,
             quantity int
         )
         '''

        insert_str = '''
         INSERT INTO cart (cart_id,cust_id,product_id,quantity)
         VALUES (%s, %s, %s, %s)
         '''
        values = (self.cart_id, self.cust_id, self.product_id, self.quantity,)

        try:
            with conn.cursor() as cursor:
                db_util.open()
                cursor.execute(create_table_str)
                cursor.execute(insert_str, values)
                conn.commit()
                print('cart inserted successfully.')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def update_cart_information(self, db_util: DBUtil,cart_id,new_cust_id,new_product_id,new_quantity ):
        conn = db_util.open()

        update_str = '''
        UPDATE cart
        SET cust_id = %s, product_id = %s, quantity = %s
        WHERE cart_id = %s
        '''
        values = (new_cust_id,new_product_id,new_quantity,cart_id)

        try:
            with conn.cursor() as cursor:
                cursor.execute(update_str, values)
                conn.commit()
                print(f'Cart with ID {cart_id} updated successfully.')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if conn.is_connected():
                conn.close()