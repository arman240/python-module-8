from geopy.distance import geodesic
airport_coordinates = {
    "EFHK": (60.317222, 24.963333),
    "EFOU": (64.930061, 25.355124), 
    "EFLP": (61.045406, 28.144369),
    "EFJO": (62.662906, 25.675655),
}
icao_code1 = input("Enter the ICAO code of the first airport: ")
icao_code2 = input("Enter the ICAO code of the second airport: ")
if icao_code1 in airport_coordinates and icao_code2 in airport_coordinates:
    coord1 = airport_coordinates[icao_code1]
    coord2 = airport_coordinates[icao_code2]
    distance = geodesic(coord1, coord2).kilometers

    print(f"The distance between {icao_code1} and {icao_code2} is approximately {distance:.2f} kilometers.")
else:
    print("One or both ICAO codes not found in the coordinates database.")