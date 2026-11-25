#creating connection with mysql database

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
     db=mysql.connector.connect(host='localhost',
               user='root',
               password=os.getenv('DB_PASSWORD'),
               database='student_management_system')
     return db