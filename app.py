from flask import Flask, request, render_template
from flask_requests import request
import mysql.connector as mysql
from flaskext.mysql import MySQL
from requests import request
import MySQLdb

app = Flask(__name__)
MYSQL = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'DATABASE PASSWORD'
app.config['MYSQL_DATABASE_DB'] = 'user_details'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
MYSQL.init_app(app)


@app.route('/', methods=[ 'GET', 'POST'])# To render Homepage
def index1():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        txtPANCard = request.form['txtPANCard ']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        cursor =mysql.connection.CursorBase()
        cursor.execute(''' INSERT INTO user_details.'user details' VALUES(%s,%s)''', (name, age,  phone, txtPANCard, address, city, state))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

    return render_template('index1.html')

def userdeatils():
    cursor = mysql.connection.CursorBase()
    cursor.execute('SELECT * FROM user details')
    registration = cursor.fetchall()
    print(registration)

userdeatils()

def alloted_limit():
    AL = 100000
    print(AL)
alloted_limit()

@app.route('/index2/', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        Loan_Amount = request.form['Loan Amount']
        Duration_of_Loan = request.form['Duration of Loan']
        rate_of_intrest = request.form['rate of intrest']
        Transaction_Date = request.form['Transaction Date']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO user_details.'transaction' VALUES(%s,%s)''', (Loan_Amount, Duration_of_Loan, rate_of_intrest, Transaction_Date))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    return  render_template('index2.html')


@app.route('/result/', methods=['GET', 'POST'])# This will be called from UI
def Interest_amount():
    cursor = mysql.connection.CursorBase()
    cursor.execute('''SELECT * FROM user_details.'transaction''VALUES(%s,%s)''')
    transaction = cursor.fetchall()

    P = input(int(transaction['Loan_Amount'])),
    T = input(float(transaction['Duration_of_Loan'])),
    R = input(int(transaction['rate_of_intrest']))

    Interest = (P * R * T) / 100
    print(Interest)


Interest_amount()


def last_date_dt():
    cursor = mysql.connection.CursorBase()
    cursor.execute('SELECT Transaction Date FROM transaction')
    transaction = cursor.fetchone()
    first_date = input(transaction['Transaction Date']),
    first_date_dt = datetime.datetime.strptime(first_date, '%d/%m/%Y'),
    lastdate = first_date_dt + datetime.timedelta(days=180),
    datetime.datetime.strftime(lastdate, '%d/%m/%Y')
    print(lastdate)


last_date_dt()

def final_amount():
    cursor = mysql.connection.CursorBase()
    cursor.execute('SELECT * FROM transaction')
    transaction = cursor.fetchall()
    P = input(int(transaction['Loan Amount'])),
    I = input(int(transaction['Interest_amount'])),
    R = input(float(transaction['rate of intrest'])),
    r = R / 100,
    t = input(int(input("Input the month : 6 "))),
    n = input(int(input("Input the month : 12 ")))

    Finalamount = P*(1 + r/n)^nt
    print(finalamount)
final_amount()



if __name__ == '__main__':
    app.run(debug=True)