import mysql.connector


def create_new_database(db_name):
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Create a database
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print("Database created")

    # Close the connection
    conn.close()


create_new_database("testdb2")
