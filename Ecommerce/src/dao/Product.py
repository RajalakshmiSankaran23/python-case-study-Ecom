def insert_product(self, db_util: DBUtil):
    conn = db_util.getconn()

    create_table_str = '''
      CREATE TABLE IF NOT EXISTS product (
          product_id INT,
          name VARCHAR(50),
          price int
      )
      '''

    insert_str = '''
      INSERT INTO product (product_id, name, price)
      VALUES (%s, %s, %s)
      '''
    values = (self.product_id, self.name, self.price)
    try:
        with conn.cursor() as cursor:
            db_util.open()
            cursor.execute(create_table_str)
            cursor.execute(insert_str, values)
            conn.commit()
            print('product inserted successfully.')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()


def update_product_information(self, db_util: DBUtil, product_id, new_name, new_price):
    conn = db_util.open()

    update_str = '''
      UPDATE product
      SET name = %s, price=%s
      WHERE product_id = %s
      '''
    values = (new_name, new_price, product_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(update_str, values)
            conn.commit()
            print(f'product with ID {product_id} updated successfully.')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()


def retrieve_product_information(self, db_util: DBUtil, product_id):
    conn = db_util.open()

    retrieve_str = '''
      SELECT product_id, name, price
      FROM product
      where product_id= %s
      '''

    values = (product_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(retrieve_str, values)
            result = cursor.fetchone()

            if result:
                product_id, name, price = result
                print(f"product ID: {product_id}")
                print(f"Name: {name}")
                print(f"price: {price}")
            else:
                print(f"product with ID {product_id} not found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()