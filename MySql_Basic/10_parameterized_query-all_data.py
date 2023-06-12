import mysql.connector


def fetch_user_data(db_name, table_name, host, user, password, username):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Fetch data for the specific user
    select_query = f'''
        SELECT * FROM {table_name}
        WHERE name = %s
    '''
    cursor.execute(select_query, (username,))

    # Fetch all rows for the user
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows


data = fetch_user_data("testdb1", "employees", "localhost", "root", "", "Batman")
for row in data:
    print(row)

"""
output:
(3, 'Batman', 35, 'IT')
"""