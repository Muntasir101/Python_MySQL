import mysql.connector


def fetch_specific_column_parameterized(db_name, table_name, column_name, host, user, password, condition):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Fetch the specific column with a parameterized query
    select_query = f'''
        SELECT {column_name} FROM {table_name}
        WHERE name = %s
    '''
    cursor.execute(select_query, (condition,))

    # Fetch all values of the column
    column_values = [row[0] for row in cursor.fetchall()]

    # Close the connection
    conn.close()

    return column_values


column_values = fetch_specific_column_parameterized("testdb1", "employees", "name", "localhost", "root", "", "Batman")
print(column_values)

"""
output:
['Batman']
"""