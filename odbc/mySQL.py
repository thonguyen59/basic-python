import mysql.connector

try:
    # Establish a connection
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='uit_cinema')
    curses = mydb.cursor()
    print("Connection successful")

    query = """select * from movie"""

    curses.execute(query)

    for row in curses:
        print(row)

    # Your code here...
except mydb.Error as ex:
    print(f"Error: {ex}")
