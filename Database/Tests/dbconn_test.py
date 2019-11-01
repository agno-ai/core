#Test connection to database server

import mysql.connector
from mysql.connector import Error



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
        print("Database name: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed \n**********************************************************")
          
