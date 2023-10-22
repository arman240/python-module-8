airport_data = {
    "EFHK": {"name": "Helsinki-Vantaa Airport", "type": "Large"},
    "EFOU": {"name": "Oulu Airport", "type": "Medium"},
    "EFET": {"name": "Enontekio Airport", "type": "Small"},
    "EFJO": {"name": "Jyvaskyla Airport", "type": "Medium"},
    "EFHE": {"name": "Helsinki-Malmi Airport", "type": "Small"},
    "EFNU": {"name": "Nurmes Airport", "type": "Small"},
    "EFHF": {"name": "Hernesaari Heliport", "type": "Helicopter"},
}
country_code = input("Enter the country area code (e.g., FI): ")
airports_by_type = {}
type_counts = {}
for icao, airport_info in airport_data.items():
    if icao.startswith(country_code):
        airport_type = airport_info["type"]
        if airport_type not in airports_by_type:
            airports_by_type[airport_type] = []
            type_counts[airport_type] = 0
        airports_by_type[airport_type].append((icao, airport_info["name"]))
        type_counts[airport_type] += 1

print(f"Airports in {country_code} ordered by type:")
for airport_type, airports in sorted(airports_by_type.items()):
    print(f"{airport_type} airports:")
    for icao, airport_name in airports:
        print(f"  - {icao}: {airport_name}")
print("\nType counts:")
for airport_type, count in type_counts.items():
    print(f"{airport_type}: {count} airports")