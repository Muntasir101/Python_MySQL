import mysql.connector


def create_table(db_name, table_name, host, user, password, ):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Create a table
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            department VARCHAR(50)
        )
    '''
    cursor.execute(create_table_query)
    print(f"Created table '{table_name}' successfully")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


create_table("testdb1", "employees", "localhost", "root", "", )
