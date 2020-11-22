import requests

# URL pulling information from, when printing (NORTH BUS ROUTES)
north_bus_url = 'https://svc.metrotransit.org/NexTrip/17940?format=json'
south_bus_url = 'http://svc.metrotransit.org/NexTrip/17928?format=json'

# DICTIONARY INCLUDES: Route, Departure, Description
def bus_routes(url):
    response = requests.get(url).json()

    # Time Departure
    for bus in response:
        route_text = bus['Route']
        departure_text = bus['DepartureText']
        description_text = bus['Description']
        print()
        print(f'Route:      Departure:      Description:')
        print(f'{route_text:<11} {departure_text:<15} {description_text:<17}')

# PRINT NORTH BUSES
message = 'Here are the North Busses:'
lines = '-' * len(message)
print(lines)
print(message)
print(lines)

# PRINT SOUTH BUSES
bus_routes(north_bus_url)
print()
message = 'Here are the South Busses:'
lines = '-' * len(message)
print(lines)
print(message)
print(lines)
bus_routes(south_bus_url)

