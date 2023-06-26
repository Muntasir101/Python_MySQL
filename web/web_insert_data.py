from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = ''
mysql_db = 'testdb2'

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)

# Create a cursor to execute MySQL queries
cursor = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']

        # Insert data into the MySQL table
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)
        conn.commit()

        return "Data inserted successfully!"

    return render_template('insert_data.html')


if __name__ == '__main__':
    app.run()
