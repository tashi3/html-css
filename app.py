# app.py (Flask example)

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration (replace with your actual credentials)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'aliza',
    'database': 'userdata'
}

# Initialize MySQL connection
db_conn = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate credentials against MySQL database
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM data WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        # Successful login
        # You can set a session or issue a token here
        return "welcome,"+username
    else:
        # Invalid credentials
        return "Invalid username or password"
    

if __name__ == '__main__':
    app.run(debug=True)
