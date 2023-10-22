import sqlite3
connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

icao_code = input("Enter the ICAO code of the airport: ")

cursor.execute("SELECT name, town FROM airport WHERE ident = ?", (icao_code,))
result = cursor.fetchone()
if result is not None:
    airport_name, airport_location = result
    print(f"Airport Name: {airport_name}")
    print(f"Airport Location (Town): {airport_location}")
else:
    print(f"No airport found with ICAO code {icao_code}")
connection.close()