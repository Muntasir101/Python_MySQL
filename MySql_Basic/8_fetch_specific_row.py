import mysql.connector


def fetch_specific_row(db_name, table_name, host, user, password, condition):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Fetch the specific row
    select_query = f'''
        SELECT * FROM {table_name}
        WHERE {condition}
    '''
    cursor.execute(select_query)

    # Fetch the row
    row = cursor.fetchone()

    # Close the connection
    conn.close()

    return row


row = fetch_specific_row("testdb1", "employees", "localhost", "root", "", "id = 1")
print(row)
