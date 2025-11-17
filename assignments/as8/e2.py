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

country=input("Enter airport country code: ")
query=f"select type,count(*) from airport where iso_country='{country}' group by type"
cursor.execute(query)
result=cursor.fetchall()
for row in result:
    print(f"Type: {row[0]}, Count: {row[1]}")
cursor.close()
connection.close()