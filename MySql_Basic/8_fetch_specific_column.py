import mysql.connector


def fetch_specific_column(db_name, table_name, column_name, host, user, password):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Fetch the specific column
    select_query = f'''
        SELECT {column_name} FROM {table_name}
    '''
    cursor.execute(select_query)

    # Fetch all values of the column
    column_values = [row[0] for row in cursor.fetchall()]

    # Close the connection
    conn.close()

    return column_values


column_values = fetch_specific_column("testdb1", "employees", "name", "localhost", "root", "")
print(column_values)
