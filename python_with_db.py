# Establishing a connection between Python and SQL with PYODBC
import pyodbc

# Establish the connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

# Check if the connection has been validated
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))

# Fetch data from Northwind DB
row = cursor.fetchone()
print(row)

# Connecting with Northwind and querying data from the Customers table
# Queries are written as a string
# fetchall() gets all the data from the table
# cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)

# Querying the Products table. Only outputting the unit price.
# prod_rows = cursor.execute("SELECT * FROM Products;").fetchall()
# for record in prod_rows:
#     print(record.UnitPrice)

# Displays each record from Products. Until there is no more data.
prod_rows = cursor.execute("SELECT * FROM Products;")
while True:
    record = prod_rows.fetchone()
    if record is None:
        break
    print(record)



# Close the connection
docker_Northwind.close()







