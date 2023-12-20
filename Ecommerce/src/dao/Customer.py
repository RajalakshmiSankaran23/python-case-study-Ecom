def insert_customer(self, db_util: DBUtil):
    conn = db_util.getconn()

    create_table_str = '''
    CREATE TABLE IF NOT EXISTS customer (
        cust_id INT,
        name VARCHAR(50),
        email VARCHAR(50),
        password VARCHAR(50)
    )
    '''

    insert_str = '''
    INSERT INTO customer (cust_id, name, email, password)
    VALUES (%s, %s, %s, %s)
    '''
    values = (self.cust_id, self.name, self.email, self.password)

    try:
        with conn.cursor() as cursor:
            db_util.open()
            cursor.execute(create_table_str)
            cursor.execute(insert_str, values)
            conn.commit()
            print('Customer inserted successfully.')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()


def update_customer_information(self, db_util: DBUtil, cust_id, new_name, new_email, new_password):
    conn = db_util.open()

    update_str = '''
    UPDATE customer
    SET name = %s, email = %s, password = %s
    WHERE cust_id = %s
    '''
    values = (new_name, new_email, new_password, cust_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(update_str, values)
            conn.commit()
            print(f'Customer with ID {cust_id} updated successfully.')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()


def retrieve_customer_information(self, db_util: DBUtil, cust_id):
    conn = db_util.open()

    retrieve_str = '''
    SELECT cust_id, name, email, password
    FROM customer
    WHERE cust_id = %s
    '''
    values = (cust_id)

    try:
        with conn.cursor() as cursor:
            cursor.execute(retrieve_str, values)
            result = cursor.fetchone()

            if result:
                cust_id, name, email, password = result
                print(f"Customer ID: {cust_id}")
                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"Password: {password}")
            else:
                print(f"Customer with ID {cust_id} not found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()


