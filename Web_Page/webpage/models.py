from datetime import datetime
from webpage import db, login_manager
from flask_login import UserMixin

import mysql.connector
mydb = mysql.connector.connect(
  host="mydatabase.clslb5ktpqun.us-east-1.rds.amazonaws.com",
  user="shudi",
  passwd="shudizhao923",
  database = "mydatabase"
)

class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    query = "SELECT * FROM mydatabase.Account WHERE email = '{}'".format(user_id)
    mydb.connect()
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    
    if result:
        user = User()
        user.id = user_id
        user.roles = result[0]['Type']
        user.name = result[0]['user_name']
        user.email = result[0]['email']
        return user
    else:
        return







