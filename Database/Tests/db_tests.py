import mysql.connector
from mysql.connector import Error
from termcolor import colored
import datetime
import time

start_time = time.time()

#**********************Test connection to database server*****************************#



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
      
        
        
		
####****************Test connection using invalid credentials******###########


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
		
        
########*************************Test selection from DB tables######################

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
        
        
################*************Test Schema Entities*****************###################

print(colored("\n--------------Starting Schema Test-----------------","blue"))

try:
    connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                         database='agno_db',
                                         user='agnoteam',
                                         password='pw4agnodb')
    if connection.is_connected():
        sql_select_Query = "SELECT * FROM information_schema.tables WHERE TABLE_SCHEMA = 'agno_db';"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        if cursor.rowcount == 0:
            print(colored('Schema test ------- FAILED', 'red'))
	
        else:
            
            
            print("Current number of tables in Database is--> ", cursor.rowcount)

            print("\nPrinting schema info\n")
            for row in records:
                print("Table Schema --> ", row[1], )
                print("Table Name --> ", row[2])
                print("Table Type --> ", row[3])
                print("Engine --> ", row[4],"\n")
		
            print(colored('Schema test ------- PASSED', 'green'))
            
        

except Error as e:
    print("Error reading data from MySQL table", e)
    print(colored('Schema test ------- FAILED', 'red'))
	
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
       
	   
####********************Push User Data to DB*************************#########


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def push_data(EntryNo, account_id, face_id,timestamp, emotion, image):
    print("Inserting data ")
    
    try:
        connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                             database='agno_db',
                                             user='agnoteam',
                                             password='pw4agnodb')

        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO Users
                          (EntryNo, account_id, face_id,timestamp, emotion, image) VALUES (%s,%s,%s,%s,%s,%s)"""

        image = convertToBinaryData(image)
       

        # Convert data to tuple format
        insert_column_data = (EntryNo, account_id, face_id,timestamp, emotion, image)
        result = cursor.execute(sql_insert_query, insert_column_data)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into Users table")
        print(colored('Push test ------- PASSED', 'green'))

    except mysql.connector.Error as error:
        print("Failed inserting data into table {}".format(error))
        print(colored('Push test ------- FAILED', 'red'))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            
            
            


print(colored("\n--------------Starting Push Test-----------------","blue"))

push_data("",1, "baer",datetime.datetime.utcnow(),
           "Happy","C:\\Users\\Sydney\\Team Project\\Database\\images\\baer.jpg")
		   
		   
		   
#***************************Test pulling data from DB*************#################


print(colored("\n--------------Starting DataPull Test-----------------","blue"))

def write_file(data, filename):
    # Convert binary data to proper format and write it to disk
    with open(filename, 'wb') as file:
        file.write(data)

def pull_data(EntryNo, image):
    print("Reading data from Users table....")

    try:
        connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                             database='agno_db',
                                             user='agnoteam',
                                             password='pw4agnodb')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from Users where EntryNo = %s"""

        cursor.execute(sql_fetch_blob_query, (EntryNo,))
        record = cursor.fetchall()
	
        if cursor.rowcount == 0:
            print(colored('Queried data is non-existent\nPull test ------- FAILED', 'red'))
	
        else:
            for row in record:
                print("EntryNo = ", row[0], )
                print("Account ID = ", row[1])
                print("Face ID = ", row[2])
                print("Timestamp = ", row[3])
                print("Emotion = ", row[4])
                photo = row[5]
                print("\nWriting image Blob to disk \n")
                write_file(photo, image)
		
            print(colored('DataPull Test ------- PASSED', 'green'))
            

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
        print(colored('Pull test ------- FAILED', 'red'))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            

pull_data(5, "C:\\Users\\Sydney\\Team Project\\Database\\images\\output\\baer.jpg")


#*****************Test pulling non-existent data***********########################


print(colored("\n--------------Starting Non-existent DataPull Test-----------------","blue"))

def write_file(data, filename):
    # Convert binary data to proper format and write it to disk
    with open(filename, 'wb') as file:
        file.write(data)

def pull_data(EntryNo, image):
    print("Reading data from Users table....")

    try:
        connection = mysql.connector.connect(host='agno-db-dev.c2witq1chtnp.eu-central-1.rds.amazonaws.com',
                                             database='agno_db',
                                             user='agnoteam',
                                             password='pw4agnodb')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from Users where EntryNo = %s"""

        cursor.execute(sql_fetch_blob_query, (EntryNo,))
        record = cursor.fetchall()
	
        if cursor.rowcount == 0:
            print(colored('Queried data is non-existent\nNon-existent DataPull Test ------- PASSED', 'green'))
	
        else:
            print(colored('Non-existent DataPull Test ------- FAILED', 'red'))
            

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
        print(colored('Non-existent DataPull Test ------- PASSED', 'green'))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


pull_data(-1, "C:\\Users\\Sydney\\Team Project\\Database\\images\\output\\ghostImage.jpg")


print("********Test Run Completed*********")
print("Total RunTime --- %s seconds ---" % round((time.time() - start_time),2))

        
