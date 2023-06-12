# insert new data time row
import mysql.connector


def add_column(db_name, table_name, host, user, password):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Add a new column for timestamp
    alter_table_query = f'''
        ALTER TABLE {table_name}
        ADD COLUMN timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    '''
    cursor.execute(alter_table_query)

    # Add a new column for date/time
    alter_table_query = f'''
        ALTER TABLE {table_name}
        ADD COLUMN datetime DATETIME DEFAULT CURRENT_TIMESTAMP
    '''
    cursor.execute(alter_table_query)
    print(f"Added column successfully on {table_name}.")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


add_column("testdb1", "user", "localhost", "root", "")
