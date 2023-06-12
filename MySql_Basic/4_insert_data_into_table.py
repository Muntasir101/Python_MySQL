import mysql.connector


def insert_data(db_name, table_name, host, user, password, data):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Insert data into the table
    insert_query = f'''
        INSERT INTO {table_name} (name, age, department)
        VALUES (%s, %s, %s)
    '''
    cursor.executemany(insert_query, data)
    print("Data inserted successfully.")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


data = [
    ('Superman', 25, 'Marketing'),
    ('Spiderman', 30, 'Sales'),
    ('Batman', 35, 'IT')
]

insert_data("testdb1", "employees", "localhost", "root", "", data)
