from flask import render_template, url_for, flash, redirect, request, session
from webpage import app, db, bcrypt
from webpage.forms import RegistrationForm, LoginForm, FlightForm, SelectFlight, ReservationForm, FlightForm2, RoundTripForm, EmpLoginForm, ReportForm, ReserveForm, AirportForm, ReceiptForm, EmployeeForm, Employee2Form, CustomerForm, Customer2Form
from webpage.models import User
from flask_login import login_user, current_user, logout_user, login_required
from wtforms import RadioField
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
  host="mydatabase.clslb5ktpqun.us-east-1.rds.amazonaws.com",
  user="shudi",
  passwd="shudizhao923",
  database = "mydatabase"
)
#Here is to build up a database for selling tickets.

#Here is post, and we can use this to build up some boxes to collect information about selling ticket. 


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
    
@app.route("/home_emp")
def home_emp():
    return render_template('home_emp.html',  status = 'employees')

@app.route("/home_cust")
def home_cust():
    return render_template('home_cust.html', status = 'customers')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        cursor = mydb.cursor(dictionary=True)
        query = "INSERT INTO mydatabase.Account VALUES ('Customer', '{user_name}','{email}','{password}', '{date}')".format(
            user_name = form.username.data, email = form.email.data, password = hashed_password, date = date.today())
        cursor.execute(query)
        mydb.commit()
        
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)




@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        mycursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM mydatabase.Account WHERE email = '{}' AND Type = 'Customer'".format(form.email.data)
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()

        if result and bcrypt.check_password_hash(result[0]['password'], form.password.data):
            user = User()
            user.id = form.email.data
            user.roles = result[0]['Type']
            user.name = result[0]['user_name']
            user.email = result[0]['email']

            login_user(user, remember=form.remember.data)
            
            return redirect(url_for('home_cust'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/EmployeeLogin", methods=['GET', 'POST'])
def EmployeeLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home_emp'))
    form = EmpLoginForm()
    if form.validate_on_submit():
        query = "SELECT * FROM mydatabase.Account WHERE email = '{}'AND Type = 'Employee'".format(form.email.data)
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()

        if result and bcrypt.check_password_hash(result[0]['password'], form.password.data):
            user = User()
            user.id = form.email.data
            user.roles = result[0]['Type']
            user.name = result[0]['user_name']
            user.email = result[0]['email']
            
            login_user(user, remember=form.remember.data)
            
            return redirect(url_for('home_emp'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('EmployeeLogin.html', title='EmployeeLogin', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/job")
@login_required
def job():
    return render_template('job.html', title='job', status = "employees")

@app.route("/oneway", methods=['GET','POST'])
@login_required
def oneway():
    form = FlightForm()
    if form.validate_on_submit():
        session['from'] = form.flying_from.data
        session['to'] = form.going_to.data
        session['date'] = form.departure_date.data
        session['meal'] = form.meal.data
        session['seat'] = form.seat.data
        session['seat_num'] = form.seat_num.data
        
        return redirect(url_for('reserve'))

    return render_template('oneway.html', title='oneway', form=form, status = "customers")

@app.route("/reserve", methods=['GET', 'POST'])
@login_required
def reserve():
    
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Stop WHERE Stop.from_airport = '{}' AND Stop.to_airport = '{}' AND Stop.dep_date = '{}' AND Stop.seat_num = '{}' ORDER BY flight_num".format(session.get('from'), session.get('to'), session.get('date'), session.get('seat_num'))
    mycursor.execute(query)#session.get('name')
    myresult = mycursor.fetchall()
    choices = [(i+1, "From: " + myresult[i]['from_airport'] + " " + "to" + " " + myresult[i]['to_airport'] +
        " " + "Departure Time:" + " " + str(myresult[i]['dep_date']) + " " + str(myresult[i]['dep_time']) + " " + "Arrival Time:" + " " +
        str(myresult[i]['arr_date']) + " " + str(myresult[i]['arr_time']) + " " + "Airline Name: " + " " + 
        myresult[i]['airline_name'] + " " + " " + " " + "Flight Number:" + " " + myresult[i]['flight_num'] + " " + 
        "Price:" + " " + "$" + str(myresult[i]['price'])) for i in range(len(myresult))] 
    form = SelectFlight()
    form.select.choices = choices

    if form.validate_on_submit():
        query1 = "INSERT INTO Reserve (airport_id, airline_name, flight_num, meal, seat, user, dep_date, arr_date, to_airport, dep_time, arr_time, price, seat_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], myresult[form.select.data - 1]['flight_num'], session.get('meal'), session.get('seat'), 
            current_user.email, myresult[form.select.data - 1]['dep_date'], myresult[form.select.data - 1]['arr_date'], myresult[form.select.data - 1]['to_airport'], myresult[form.select.data - 1]['dep_time'], 
            myresult[form.select.data - 1]['arr_time'], myresult[form.select.data - 1]['price'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query1)   
        query2 = "DELETE FROM Stop WHERE Stop.airport_id = '{}' AND Stop.airline_name = '{}' AND Stop.flight_num = '{}' AND Stop.seat_num = '{}'".format(myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], 
            myresult[form.select.data - 1]['flight_num'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query2)   
        mydb.commit()
        return redirect(url_for('finish'))
    return render_template('reserve.html', title = 'Reserve', result=myresult, form=form, status = 'customers')

@app.route("/MyReservation", methods=['GET', 'POST'])
@login_required
def MyReservation():
    print(current_user.email)
    mycursor = mydb.cursor(dictionary=True)
    query3 = "SELECT * FROM Reserve WHERE Reserve.user = '{}'".format(current_user.email)
    mycursor.execute(query3)
    myresult = mycursor.fetchall()
    choices = [(i+1, "From: " + myresult[i]['airport_id'] + " " + "to" + " " + myresult[i]['to_airport'] +
        " " + "Departure Time:" + " " + str(myresult[i]['dep_date']) + " " + str(myresult[i]['dep_time']) + " " + "Arrival Time:" + " " +
        str(myresult[i]['arr_date']) + " " + str(myresult[i]['arr_time']) + " " + "Airline Name: " + " " + 
        myresult[i]['airline_name'] + " " + " " + " " + "Flight Number:" + " " + myresult[i]['flight_num'] + " " + 
        "Price:" + " " + "$" + str(myresult[i]['price'])) for i in range(len(myresult))]
    print(choices) 
    form = ReservationForm()
    form.select.choices = choices
    if form.validate_on_submit():
        query4 = "INSERT INTO Stop (airport_id, airline_name, flight_num, dep_date, arr_date, to_airport, dep_time, arr_time, price, from_airport, seat_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], myresult[form.select.data - 1]['flight_num'],  
            myresult[form.select.data - 1]['dep_date'], myresult[form.select.data - 1]['arr_date'], myresult[form.select.data - 1]['to_airport'], myresult[form.select.data - 1]['dep_time'], 
            myresult[form.select.data - 1]['arr_time'], myresult[form.select.data - 1]['price'], myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query4)   
        query5 = "DELETE FROM Reserve WHERE Reserve.airport_id = '{}' AND Reserve.airline_name = '{}' AND Reserve.flight_num = '{}' AND Reserve.seat_num = '{}'".format(myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], 
            myresult[form.select.data - 1]['flight_num'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query5)   
        mydb.commit()
        return redirect(url_for('complete'))
    return render_template('MyReservation.html', title = 'MyReservation', result=myresult, form=form, status = "customers")

@app.route("/roundtrip", methods=['GET','POST'])
@login_required
def roundtrip():
    form = FlightForm2()
    if form.validate_on_submit():
        session['from'] = form.flying_from.data
        session['to'] = form.going_to.data
        session['departure_date'] = form.departure_date.data
        session['meal'] = form.meal.data
        session['seat'] = form.seat.data
        session['return_date'] = form.return_date.data
        session['seat_num'] = form.seat_num.data
        return redirect(url_for('departure'))
    return render_template('roundtrip.html', title='roundtrip', form=form, status = "customers")

@app.route("/departure", methods=['GET', 'POST'])
@login_required
def departure():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Stop WHERE Stop.from_airport = '{}' AND Stop.to_airport = '{}' AND Stop.dep_date = '{}' AND Stop.seat_num = '{}' ORDER BY flight_num".format(
        session.get('from'), session.get('to'), session.get('departure_date'), session.get('seat_num'))
    mycursor.execute(query)#session.get('name')
    myresult = mycursor.fetchall()
    choices = [(i+1, "From: " + myresult[i]['from_airport'] + " " + "to" + " " + myresult[i]['to_airport'] +
        " " + "Departure Time:" + " " + str(myresult[i]['dep_date']) + " " + str(myresult[i]['dep_time']) + " " + "Arrival Time:" + " " +
        str(myresult[i]['arr_date']) + " " + str(myresult[i]['arr_time']) + " " + "Airline Name: " + " " + 
        myresult[i]['airline_name'] + " " + " " + " " + "Flight Number:" + " " + myresult[i]['flight_num'] + " " + 
        "Price:" + " " + "$" + str(myresult[i]['price'])) for i in range(len(myresult))] 
    form = RoundTripForm()
    form.select.choices = choices
    if form.validate_on_submit():
        query1 = "INSERT INTO Reserve (airport_id, airline_name, flight_num, meal, seat, user, dep_date, arr_date, to_airport, dep_time, arr_time, price, seat_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], myresult[form.select.data - 1]['flight_num'], session.get('meal'), session.get('seat'), 
            current_user.email, myresult[form.select.data - 1]['dep_date'], myresult[form.select.data - 1]['arr_date'], myresult[form.select.data - 1]['to_airport'], myresult[form.select.data - 1]['dep_time'], 
            myresult[form.select.data - 1]['arr_time'], myresult[form.select.data - 1]['price'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query1)   
        query2 = "DELETE FROM Stop WHERE Stop.airport_id = '{}' AND Stop.airline_name = '{}' AND Stop.flight_num = '{}' AND Stop.seat_num = '{}'".format(myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], 
            myresult[form.select.data - 1]['flight_num'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query2)   
        mydb.commit()
        return redirect(url_for('returning'))
    return render_template('departure.html', title = 'departure', result=myresult, form=form,  status = 'customers')

@app.route("/returning", methods=['GET', 'POST'])
@login_required
def returning():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Stop WHERE Stop.dep_date = '{}' AND Stop.from_airport = '{}' AND Stop.to_airport = '{}' AND Stop.seat_num = '{}' ORDER BY flight_num".format(
        session.get('return_date'), session.get('to'), session.get('from'), session.get('seat_num'))
    mycursor.execute(query)#session.get('name')
    myresult = mycursor.fetchall()
    choices = [(i+1, "From: " + myresult[i]['from_airport'] + " " + "to" + " " + myresult[i]['to_airport'] +
        " " + "Departure Time:" + " " + str(myresult[i]['dep_date']) + " " + str(myresult[i]['dep_time']) + " " + "Arrival Time:" + " " +
        str(myresult[i]['arr_date']) + " " + str(myresult[i]['arr_time']) + " " + "Airline Name: " + " " + 
        myresult[i]['airline_name'] + " " + " " + " " + "Flight Number:" + " " + myresult[i]['flight_num'] + " " + 
        "Price:" + " " + "$" + str(myresult[i]['price'])) for i in range(len(myresult))] 
    form = RoundTripForm()
    form.select.choices = choices
    if form.validate_on_submit():
        query1 = "INSERT INTO Reserve (airport_id, airline_name, flight_num, meal, seat, user, dep_date, arr_date, to_airport, dep_time, arr_time, price, seat_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], myresult[form.select.data - 1]['flight_num'], session.get('meal'), session.get('seat'), 
            current_user.email, myresult[form.select.data - 1]['dep_date'], myresult[form.select.data - 1]['arr_date'], myresult[form.select.data - 1]['to_airport'], myresult[form.select.data - 1]['dep_time'], 
            myresult[form.select.data - 1]['arr_time'], myresult[form.select.data - 1]['price'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query1)   
        query2 = "DELETE FROM Stop WHERE Stop.airport_id = '{}' AND Stop.airline_name = '{}' AND Stop.flight_num = '{}' AND Stop.seat_num = '{}'".format(myresult[form.select.data - 1]['airport_id'], myresult[form.select.data - 1]['airline_name'], 
            myresult[form.select.data - 1]['flight_num'], myresult[form.select.data - 1]['seat_num'])
        mycursor.execute(query2)   
        mydb.commit()
        return redirect(url_for('finish'))
    return render_template('returning.html', title = 'returning', result=myresult, form=form,  status = 'customers')

@app.route("/salesreport", methods=['GET','POST'])
@login_required
def salesreport():
    form = ReportForm()
    if form.validate_on_submit():
        session['month'] = form.month.data
        return redirect(url_for('result'))
    return render_template('salesreport.html', title='salesreport', form=form, status = 'employees')

@app.route("/result", methods=['GET','POST'])
@login_required
def result():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT SUM(Reserve.price) FROM Reserve WHERE Reserve.dep_date LIKE '_____{}___'".format(session.get('month'))
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return render_template('result.html', result = myresult, status = 'employees')

@app.route("/reservations", methods=['GET','POST'])
@login_required
def reservations():
    form = ReserveForm()
    if form.validate_on_submit():
        session['flight'] = form.flight_num.data
        return redirect(url_for('result2'))
    return render_template('reservations.html', title='reservations', form=form, status = 'employees')

@app.route("/result2", methods=['GET','POST'])
@login_required
def result2():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Reserve WHERE Reserve.flight_num = '{}' ".format(session.get('flight'))
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    query2 = "SELECT DISTINCT * FROM Flight WHERE Flight.flight_num = '{}' ".format(session.get('flight'))
    mycursor.execute(query2)
    myresult2 = mycursor.fetchall()
    return render_template('result2.html', result = myresult, result2 = myresult2, status = 'employees')

@app.route("/revenue", methods=['GET','POST'])
@login_required
def revenue():
    form = ReserveForm()
    if form.validate_on_submit():
        session['flight1'] = form.flight_num.data
        return redirect(url_for('result3'))
    return render_template('revenue.html', title='revenue', form=form, status = 'employees')

@app.route("/result3", methods=['GET','POST'])
@login_required
def result3():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT SUM(Reserve.price) FROM Reserve WHERE Reserve.flight_num = '{}'".format(session.get('flight'))
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)
    return render_template('result3.html', result = myresult, status = 'employees')

@app.route("/result6", methods=['GET','POST'])
@login_required
def result6():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT Reserve.User FROM Reserve GROUP BY Reserve.User HAVING SUM(Reserve.price) >= ALL(SELECT SUM(R.price) FROM Reserve AS R Group BY R.User)"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    query2 = "SELECT DISTINCT Account.user_name FROM Account WHERE Account.Type = 'Customer' AND Account.email = '{}'".format(myresult[0]['User'])
    mycursor.execute(query2)
    myresult2 = mycursor.fetchall()
    return render_template('result6.html', result = myresult, result2 = myresult2, status = 'employees')

@app.route("/result7", methods=['GET','POST'])
@login_required
def result7():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT DISTINCT Stop.flight_num FROM Stop GROUP BY Stop.flight_num HAVING COUNT(*) >= ALL(SELECT COUNT(*) FROM Stop AS S GROUP BY S.flight_num)"
    mycursor.execute(query)
    myresult1 = mycursor.fetchall()
    querys = "SELECT DISTINCT Stop.airport_id, Stop.dep_date, Stop.arr_date, Stop.airline_name, Stop.flight_num, Stop.from_airport, Stop.to_airport, Stop.dep_time, Stop.arr_time, Stop.price FROM Stop WHERE Stop.flight_num = '{}'".format(myresult1[0]['flight_num'])
    mycursor.execute(querys)
    myresult = mycursor.fetchall()
    return render_template('result7.html', result = myresult, status = 'employees')

@app.route("/result8", methods=['GET','POST'])
@login_required
def result8():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT DISTINCT Reserve.User FROM Reserve"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return render_template('result8.html', result = myresult, status = 'employees')

@app.route("/q9", methods=['GET','POST'])
@login_required
def q9():
    form = AirportForm()
    if form.validate_on_submit():
        session['airport'] = form.airport.data
        return redirect(url_for('result9'))
    return render_template('q9.html', title='q9', form=form, status = 'employees')

@app.route("/result9", methods=['GET','POST'])
@login_required
def result9():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT DISTINCT Stop.airport_id, Stop.dep_date, Stop.arr_date, Stop.airline_name, Stop.flight_num, Stop.from_airport, Stop.to_airport, Stop.dep_time, Stop.arr_time, Stop.price FROM Stop WHERE Stop.airport_id = '{}' ".format(session.get('airport'))
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    query2 = "SELECT Airports.name FROM Airports WHERE Airports.airport_id = '{}' ".format(session.get('airport'))
    mycursor.execute(query2)
    myresult2 = mycursor.fetchall()
    print(myresult2)
    return render_template('result9.html', result = myresult, result2 = myresult2, status = 'employees')


@app.route("/allflights", methods=['GET','POST'])
@login_required
def allflights():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT DISTINCT Stop.flight_num, Stop.price, Stop.arr_date, Stop.arr_time, Stop.dep_time, Stop.dep_date, Stop.from_airport, Stop.to_airport, Stop.airline_name, Stop.flight_num FROM Stop"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return render_template('allflights.html', result = myresult, status = 'employees')

@app.route("/receipt", methods=['GET','POST'])
@login_required
def receipt():
    form = ReceiptForm()
    if form.validate_on_submit():
        session['user'] = form.user.data
        return redirect(url_for('result10'))
    return render_template('receipt.html', title='receipt', form=form, status = 'employees')

@app.route("/result10", methods=['GET','POST'])
@login_required
def result10():
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Reserve WHERE Reserve.User = '{}' ".format(session.get('user'))
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return render_template('result10.html', result = myresult, status = 'employees')

@app.route("/addemp", methods=['GET','POST'])
@login_required
def addemp():
    form = EmployeeForm()
    if form.validate_on_submit():
        mycursor = mydb.cursor(dictionary=True)
        query11 = "INSERT INTO Employee VALUES ('{first_name}', '{last_name}', '{email}', '{SSN}', '{Address}', '{city}', '{state}', '{zip_code}', '{telephone}', '{start_date}', '{hourly_rate}', '{password}')".format(first_name = form.first_name.data, last_name = form.last_name.data, email=form.email.data, SSN=form.ssn.data, Address=form.street.data, city=form.city.data, state=form.state.data, zip_code=form.zip_code.data, telephone=form.telephone.data, start_date=date.today(), hourly_rate=form.hourly_rate.data, password=form.password.data)
        mycursor.execute(query11)
        hashed_password2 = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        query12 = "INSERT INTO Account VALUES('Employee','{user_name}','{email}','{password}','{date}')".format(user_name=form.first_name.data, email=form.email.data,password=hashed_password2, date=date.today())
        mycursor.execute(query12)
        mydb.commit()
        return redirect(url_for('result11'))
    return render_template('addemp.html', title='addemp', form=form, status = 'employees')

@app.route("/result11")
@login_required
def result11():
    return render_template('result11.html', status = 'employees')

@app.route("/delemp", methods=['GET','POST'])
@login_required
def delemp():
    form = Employee2Form()
    if form.validate_on_submit():
        mycursor = mydb.cursor(dictionary=True)
        query11 = "DELETE FROM Employee WHERE Employee.SSN = '{}'".format(form.ssn.data)
        mycursor.execute(query11)
        query12 = "DELETE FROM Account WHERE Account.Type = 'Employee' AND Account.email = '{}' ".format(form.email.data)
        mycursor.execute(query12)
        mydb.commit()
        return redirect(url_for('result12'))
    return render_template('delemp.html', title='delemp', form=form, status = 'employees')

@app.route("/result12")
@login_required
def result12():
    return render_template('result12.html', status = 'employees')

@app.route("/addcust", methods=['GET','POST'])
@login_required
def addcust():
    form = CustomerForm()
    if form.validate_on_submit():
        mycursor = mydb.cursor(dictionary=True)
        query11 = "INSERT INTO Customer VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(form.first_name.data, form.email.data, form.last_name.data, form.street.data, form.city.data, form.state.data, form.zip_code.data, form.credit_card.data, form.telephone.data)
        mycursor.execute(query11)
        mydb.commit()
        return redirect(url_for('result13'))
    return render_template('addcust.html', title='addcust', form=form, status = 'employees')

@app.route("/result13")
@login_required
def result13():
    return render_template('result13.html', status = 'employees')

@app.route("/delcust", methods=['GET','POST'])
@login_required
def delcust():
    form = Customer2Form()
    if form.validate_on_submit():
        mycursor = mydb.cursor(dictionary=True)
        query11 = "DELETE FROM Customer WHERE Customer.first_name = '{}' AND Customer.email = '{}' ".format(form.first_name.data, form.email.data)
        mycursor.execute(query11)
        mydb.commit()
        return redirect(url_for('result14'))
    return render_template('delcust.html', title='delcut', form=form, status = 'employees')

@app.route("/result14")
@login_required
def result14():
    return render_template('result14.html', status = 'employees')

@app.route("/finish")
@login_required
def finish():
    return render_template('/finish.html',  status = 'customers')

@app.route("/complete")
@login_required
def complete():
    return render_template('/complete.html', status = 'customers')

