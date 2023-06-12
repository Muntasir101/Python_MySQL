import mysql.connector


def fetch_all_data(db_name, table_name, host, user, password):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Fetch all row data
    select_query = f'''
        SELECT * FROM {table_name}
    '''
    cursor.execute(select_query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows


data = fetch_all_data("testdb1", "employees", "localhost", "root", "")
for row in data:
    print(row)
"""
Output:
(1, 'Superman', 25, 'Marketing')
(2, 'Spiderman', 30, 'Sales')
(3, 'Batman', 35, 'IT'
"""
