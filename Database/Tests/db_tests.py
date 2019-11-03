

import mysql.connector
from mysql.connector import Error
from termcolor import colored
import datetime


#Test connection to database server



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
		
        
#Test selection from DB tables

print(colored("\n--------------Starting SELECT Query Test-----------------","blue"))

try:
    connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                         database='agno_db',
                                         user='agnoteam',
                                         password='pw4agnodb')
    if connection.is_connected():
        sql_select_Query = "select * from Users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of records in Users table  is: ", cursor.rowcount)

        print("\nPrinting each User record\n")
        for row in records:
            print("EntryNo --> ", row[0], )
            print("accound_id --> ", row[1])
            print("face_id --> ", row[2])
            print("Timestamp --> ", row[3])
            print("Emotion --> ", row[4], "\n")
        
        print(colored('SELECT Query test ------- PASSED', 'green'))
            
        

except Error as e:
    print("Error reading data from MySQL table", e)
    print(colored('SELECT Query test ------- FAILED', 'red'))
	
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
