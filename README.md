# Python with SQL
### Apply CRUD
`create`, `read`, `update`, `delete`
### Making data persistent
### Establishing a connection with PYODBC
The following code establishes a connection from the 
`Northwind` database and Python, with `pyodbc`. 
```python
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
```

If the connection doesn't work, install the dependencies from
[this link](https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15)
and follow the instructions for your OS.

To check if your connection has been validated, create a 
`cursor` from your connection and run an initial query.
```python
# Check if the connection has been validated
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))
```

The following will query the Customers table. The `fetchall()`
method gets all the records from the table and outputting
the result will display the records on a single line.
```python
# Connecting with Northwind and querying data from the Customers table
# Queries are written as a string
# fetchall() gets all the data from the table
cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
print(cust_rows)
```

The following code fetches all the records from the Products 
table, then outputs each record's UnitPrice on a separate line. 
```python
# Querying the Products table. Only outputting the unit price.
prod_rows = cursor.execute("SELECT * FROM Products;").fetchall()
for record in prod_rows:
    print(record.UnitPrice)
```

The following code does the same as above, but uses a `while`
loop instead. It displays each record until there are none
left using `fetchone()`.
````python
# Displays each record from Products. Until there is no more data.
prod_rows = cursor.execute("SELECT * FROM Products;")
while True:
    record = prod_rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
````



