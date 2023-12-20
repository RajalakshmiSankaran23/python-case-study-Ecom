from Ecommerce.src.util.DButil import DBUtil

db_util = DBUtil()

conn = db_util.getconn()

create_table_str = '''
    CREATE TABLE IF NOT EXISTS customer (
        cust_id INT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
'''

try:
    with conn.cursor() as cursor:
        cursor.execute(create_table_str)
    conn.commit()
    print("Customers table created successfully.")
except Exception as e:
    print(f"Error creating customers table: {e}")
