#creating connection with mysql database
import mysql.connector
def get_connection():
     db=mysql.connector.connect(host='localhost',
               user='root',
               password='Sfarhan@1408',
               database='student_management_system')
     return db