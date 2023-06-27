from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb3"
)
cursor = db.cursor()


@app.route('/')
def index():
    # Fetch all records from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Insert new record into the database
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        return redirect('/')
    return render_template('add.html')


@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    # Fetch the record to be edited from the database
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Update the record in the database
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        db.commit()
        return redirect('/')
    return render_template('edit.html', user=user)


@app.route('/delete/<int:user_id>')
def delete(user_id):
    # Delete the record from the database
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
