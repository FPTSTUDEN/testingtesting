import mysql.connector
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="flight_game"
    )
    return connection
ident=input("Enter airport ICAO code: ")
connection=connect_to_db()
cursor=connection.cursor()
query="select name, iso_region from airport where ident=%s"
cursor.execute(query,(ident,))
result=cursor.fetchone()
if result:
    print("Airport name:", result[0])
    print("ISO Region:", result[1])
else:
    print("No airport found")
cursor.close()
connection.close()