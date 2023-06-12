import mysql.connector


def fetch_all_data_list(db_name, table_name, host, user, password):
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

    # Create separate lists for each column value
    column_lists = [[] for _ in range(len(rows[0]))]
    for row in rows:
        for i, value in enumerate(row):
            column_lists[i].append(value)

    return column_lists


data_lists = fetch_all_data_list("testdb1", "employees", "localhost", "root", "")

# Print each column list
for column_list in data_lists:
    print(column_list)


"""
output:
[1, 2, 3]
['Superman', 'Spiderman', 'Batman']
[25, 30, 35]
['Marketing', 'Sales', 'IT']
"""