airports = {
    "EFHK": "Helsinki-Vantaa",
    "EFOU": "Oulu",
    "EFRO": "Rovaniemi"
}
while (cmd := input("Add new airport, fetch name by code, or quit (a/f/q): ")) != "q":
    if cmd == "a":
        code = input("Enter airport code: ")
        name = input("Enter airport name: ")
        airports[code] = name
    elif cmd == "f":
        code = input("Enter airport code to fetch: ")
        print(airports.get(code, "Airport code not found"))