import mysql.connector


def get_connected_db_info(database, host, user, password, ):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Fetch the connected database information
        connected_db = connection.database

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

        # Close the connection
        connection.close()

        return connected_db

    except mysql.connector.Error as err:
        print("Error:", err)

        return None


connected_db = get_connected_db_info("testdb1", "localhost", "root", "")

"""
Output:
Connected to MySQL Server version  5.5.5-10.4.28-MariaDB
You're connected to database:  ('testdb1',)
"""
