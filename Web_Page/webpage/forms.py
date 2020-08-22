from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webpage.models import User

# Username cannot be empty; min 2; max 20. 
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)] )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

'''    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')'''


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class EmpLoginForm(FlaskForm):
    email = StringField('Employee Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),  Length(min=6, max=25)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class FlightForm(FlaskForm):
    
    flying_from = SelectField('Leaving from', choices=[('ORD', "O'Hare International Airport"), ('LGA', 'LaGuardia Airport'), ('LAX', 'Los Angeles International Airport'), ('DFW', 'Dallas/Fort Worth International Airport')])
    going_to = SelectField('Going to', choices=[('ORD', "O'Hare International Airport"), ('LGA', 'LaGuardia Airport'), ('LAX', 'Los Angeles International Airport'), ('DFW', 'Dallas/Fort Worth International Airport')])
    #departure_date = DateField('Departure date (format: year-month-day, ####-##-##)', format="%Y-%m-%d")
    departure_date = SelectField('Departure date', choices=[('2020-09-01', '09/01/2020'), ('2020-09-09', '09/09/2020'), ('2020-09-13', '09/13/2020'), ('2020-09-15', '09/15/2020'), ('2020-09-20', '09/20/2020'),('2020-09-23', '09/23/2020'),('2020-10-18', '10/18/2020'),('2020-10-20', '10/20/2020')])
    meal = SelectField('Please choose your meal:', choices=[('lobster', 'Lobster'), ('steak', 'Steak'), ('salad','Salad'), ('sandwich', 'Sandwich'), ('shirmp', 'Shirmp')])
    seat = SelectField('Please choose your seat:', choices=[('aisle','Aisle'), ('window', 'Window'), ('middle', 'Middle')])
    seat_num = SelectField('Choose your seat Number:', choices=[('1', 'Number 1'), ('2', 'Number 2'), ('3', 'Number 3'), ('4', 'Number 4'), ('5', 'Number 5'), ('6', 'Number 6')])
    submit = SubmitField('Search')


class SelectFlight(FlaskForm):
    select = RadioField("Select A Flight:", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Reserve")

class ReservationForm(FlaskForm):
    select = RadioField("You can select the flight that you want to cancel it:", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Confirm")

class RoundTripForm(FlaskForm):
    select = RadioField("Select A Flight:", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Reserve")


class FlightForm2(FlaskForm):

    flying_from = SelectField('Leaving from', choices=[('ORD', "O'Hare International Airport"), ('LGA', 'LaGuardia Airport'), ('LAX', 'Los Angeles International Airport'), ('DFW', 'Dallas/Fort Worth International Airport')])
    going_to = SelectField('Going to', choices=[('ORD', "O'Hare International Airport"), ('LGA', 'LaGuardia Airport'), ('LAX', 'Los Angeles International Airport'), ('DFW', 'Dallas/Fort Worth International Airport')])
    #departure_date = DateField('Departure date (format: year-month-day, ####-##-##)', format="%Y-%m-%d")
    #return_date = DateField('Returing date (format: year-month-day, ####-##-##)', format="%Y-%m-%d")
    departure_date = SelectField('Departure date', choices=[('2020-09-01', '09/01/2020'), ('2020-09-09', '09/09/2020'), ('2020-09-20', '09/20/2020'),('2020-09-23', '09/23/2020')])
    return_date = SelectField('Departure date', choices=[('2020-09-13', '09/13/2020'), ('2020-09-15', '09/15/2020'), ('2020-10-18', '10/18/2020'),('2020-10-20', '10/20/2020')])
    meal = SelectField('Please choose your meal:', choices=[('lobster', 'Lobster'), ('steak', 'Steak'), ('salad','Salad'), ('sandwich', 'Sandwich'), ('shirmp', 'Shirmp')])
    seat = SelectField('Please choose your seat:', choices=[('aisle','Aisle'), ('window', 'Window'), ('middle', 'Middle')])
    seat_num = SelectField('Choose your seat Number:', choices=[('1', 'Number 1'), ('2', 'Number 2'), ('3', 'Number 3'), ('4', 'Number 4'), ('5', 'Number 5'), ('6', 'Number 6')])
    submit = SubmitField('Search')


class ReportForm(FlaskForm):
    month = SelectField('Month of the report', choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')])
    submit = SubmitField('Search')

class ReserveForm(FlaskForm):
    flight_num = SelectField('Flight Number', choices=[('0001', '0001'),('0002','0002'),('0003', '0003'),
        ('0012', '0012'),('0021', '0021'), ('0031','0031'),('0049','0049'),('0056','0056'),('0078','0078'),
        ('0220','0220'),('0231','0231'),('0327','0327'),('0563','0563'),('0578', '0578'),('0671','0671'),
        ('1257', '1257'),('3451', '3451'),('3468', '3468'),('4512', '4512'),('5347', '5347'),('5721', '5721'),
        ('6894', '6894'),('7612', '7612'),('9745', '9745')])
    submit = SubmitField('Search')
class AirportForm(FlaskForm):
    airport = SelectField('Airport Name:', choices=[('ORD', "O'Hare International Airport"), ('LGA', 'LaGuardia Airport'), ('LAX', 'Los Angeles International Airport'), ('DFW', 'Dallas/Fort Worth International Airport')])
    submit = SubmitField('Search')

class ReceiptForm(FlaskForm):
    user = StringField('User Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Search')

class EmployeeForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Employee login Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Employee login Password', validators=[DataRequired(), Length(min=6, max=25)])
    ssn = StringField('SSN:', validators=[DataRequired(), Length(min=9, max=9)])
    telephone = StringField('Telephone', validators=[DataRequired(), Length(min=10, max=10)])
    hourly_rate = StringField('Hourly Rate', validators=[DataRequired(), Length(min=1, max=8)])
    street = StringField('Street Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired(), Length(min=5, max=10)])
    submit = SubmitField('Add')

class Employee2Form(FlaskForm):
    ssn = StringField('SSN:', validators=[DataRequired(), Length(min=9, max=9)])
    email = StringField('Employee login Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Delete')

class CustomerForm(FlaskForm):
    first_name = StringField('First  name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    telephone = StringField('Telephone', validators=[DataRequired(), Length(min=10, max=10)])
    credit_card = StringField('Credit_card', validators=[DataRequired(), Length(min=16, max=16)])
    street = StringField('Street Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired(), Length(min=5, max=10)])
    submit = SubmitField('Add')

class Customer2Form(FlaskForm):
    first_name = StringField('First  name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Delete')
