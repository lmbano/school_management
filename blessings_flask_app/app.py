from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'student_db'

mysql = MySQL(app)

# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['username'] = user['username']
            return redirect(url_for('student_records'))  # Redirect to student_records after login
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Student Records Route
@app.route('/student_records', methods=['GET', 'POST'])
def student_records():
    if 'loggedin' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        if 'add' in request.form:
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            cursor.execute('INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)', (name, age, grade))
            mysql.connection.commit()
            flash('Student added successfully!', 'success')
        elif 'edit' in request.form:
            student_id = request.form['id']
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            cursor.execute('UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s', (name, age, grade, student_id))
            mysql.connection.commit()
            flash('Student updated successfully!', 'success')
        elif 'delete' in request.form:
            student_id = request.form['id']
            cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
            mysql.connection.commit()
            flash('Student deleted successfully!', 'success')
    
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return render_template('student_records.html', students=students)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
