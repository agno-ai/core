#Test connection to database server

import mysql.connector
from mysql.connector import Error
from termcolor import colored
import datetime


print(colored("--------------Starting Connection Test-----------------","blue"))

try:
    connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                         database='agno_db',
                                         user='agnoteam',
                                         password='pw4agnodb')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Successfully connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database name: ", record,)
        print(colored('Connection test ------- PASSED', 'green'))

except Error as e:
    print("Connection Test Failed", e)
    print(colored('Connection test---------- FAILED', 'red'))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
      
        
        
		
#Test connection using invalid credentials


print(colored("\n--------------Starting Invalid credentials testing-----------------","blue"))

try:
    connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                         database='agno_db',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Successfully connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database name: ", record,)
        print(colored('Connection test ------- FAILED', 'red'))

except Error as e:
    print("Credential Test Passed", e)
    print(colored('Credential Test--------- PASSED', 'green'))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
