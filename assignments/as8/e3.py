import mysql.connector
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="flight_game",
        port=3306
    )
    return connection

connection=connect_to_db()
cursor=connection.cursor()

icao1=input("Enter first airport ICAO code: ")
icao2=input("Enter second airport ICAO code: ")

from geopy import distance

query="select latitude_deg, longitude_deg from airport where ident=%s"
cursor.execute(query,(icao1,))
result1=tuple(i for i in cursor.fetchone())
cursor.execute(query,(icao2,))
result2=tuple(i for i in cursor.fetchone())
dist=distance.distance(result1,result2).km
print(f"Distance between {icao1} and {icao2} is {dist:.2f} km")

cursor.close()
connection.close()