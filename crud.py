import pyodbc
import sys
server = 'localhost'
database = 'demodb'
username = 'sa'
password = 'P2ssw0rd'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO demos (demo_id, demo_name, demo_desc) VALUES (?,?,?);"
with cursor.execute(tsql,'3','create asp.net app build', 'Pipeline for building the ASP.NET application'):
    print ('Successfully Inserted!')

#Update Query
print ('Updating lst row')
tsql = "UPDATE demos SET demo_name = ? WHERE demo_name = ?"
with cursor.execute(tsql,'create asp.net web app build pipeline','create asp.net app build'):
    print ('Successfully Updated!')


#Delete Query
print ('Deleting last row')
tsql = "DELETE FROM demos WHERE demo_id = ?"
with cursor.execute(tsql,'3'):
    print ('Successfully Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT * FROM demos;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        row = cursor.fetchone()