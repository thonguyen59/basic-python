import pyodbc

DRIVER = 'SQL Server'
SERVER = 'GROOO0030'
DATABASE = 'BikeStores5'

# Correct the formatting of the connection string
str_sql = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=1'

try:
    # Establish a connection
    print(str_sql)
    cnxn = pyodbc.connect(str_sql)
    curses = cnxn.cursor()
    print("Connection successful")

    query = """select * from sales.customers"""

    curses.execute(query)

    for row in curses:
        print(row)

    # Your code here...
except pyodbc.Error as ex:
    print(f"Error: {ex}")
