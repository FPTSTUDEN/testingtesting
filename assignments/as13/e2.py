# http://127.0.0.1:5000/airport/EFHK
# {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}
import mysql.connector
from flask import Flask, jsonify
app = Flask(__name__)
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='flight_game'
    )
    return connection
@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT ident, name, municipality FROM airport WHERE ident=%s"
    cursor.execute(query, (icao,))
    airport = cursor.fetchone()
    cursor.close()
    connection.close()

    if airport:
        return jsonify({
            'ICAO': airport['ident'],
            'Name': airport['name'],
            'Location': airport['municipality']
        })
    else:
        return jsonify({'error': 'Airport not found'}), 404
if __name__ == "__main__":
    app.run(debug=True)