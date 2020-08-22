# Web_Page

This is a flight reservation  web page called  itravel that written in Python flask. 
Users need to create a customer account in order to make flight reservations(one way or round trip). Customers
can also review all the reservations they made and cancel the reservations they don't want. Employees can login with
their existing employee account to do their jobs such as add an employee, delete an employee, add a customer, delete 
a customer, generate the sales report for a specific month, list all flights, check reservations by flight number, 
generate revenue summary by flight number, find the customer who generated the most revenus, find the most active 
flight, return all the customers who made an reservation on our website, list all the flight for a given airport, 
and generate the customer receipt. The data is stored in MySQL database that are connected with Amazon RDS(MySQL 
database). And the application is running on EC2. 

I used seven tables for this application. Account table stored all the login informations like email, username, 
password, creation date, and login type(employee or customer). Airports table stores all the airports informations like
airport id, airport name, country, and city. Customer table stores all the customer informations like first name, last 
name, address, email, credit card, and phone number. Employee table stores all the employee informations like first name, 
last name, email, SSN, address, phone number, hourly rate, hired date, and password for employee login. Flight table has
all the basic flight informations like airline id, flight number, airline. Reserve table has all the reservations made by 
every customer. Stop table has all the detailed informations about each flight, which is the table that customer make
reservations based on. 
