# WeatherServer.py
# Run this program before running WeatherClient.py.

import socket

HOST = "127.0.0.1"   # Allows the client on this same computer to connect
PORT = 12345 # <------ You will need to change this numer!!!!

# Each city is stored as:
# City|Country|Coordinates|TemperatureC|TemperatureF
weather_data = [
    "Toronto|Canada|43.6532,-79.3832|12|53",
    "London|United Kingdom|51.5072,-0.1276|15|59",
    "Tokyo|Japan|35.6762,139.6503|21|70",
    "New York|United States|40.7128,-74.0060|18|64",
    "Sydney|Australia|-33.8688,151.2093|24|75",
    "Paris|France|48.8566,2.3522|16|61",
    "Rome|Italy|41.9028,12.4964|22|72",
    "Dubai|United Arab Emirates|25.2048,55.2708|35|95",
    "Vancouver|Canada|49.2827,-123.1207|14|57",
    "Calgary|Canada|51.0447,-114.0719|9|48",
    "Miami|United States|25.7617,-80.1918|29|84",
    "Los Angeles|United States|34.0522,-118.2437|25|77",
    "Berlin|Germany|52.5200,13.4050|11|52",
    "Madrid|Spain|40.4168,-3.7038|27|81",
    "Cairo|Egypt|30.0444,31.2357|32|90",
    "Seoul|South Korea|37.5665,126.9780|19|66",
    "Mumbai|India|19.0760,72.8777|31|88",
    "Auckland|New Zealand|-36.8509,174.7645|17|63",
    "Reykjavik|Iceland|64.1466,-21.9426|5|41",
    "Mexico City|Mexico|19.4326,-99.1332|23|73"
]


def send_weather_data(client):
    # Send each city as one line.
    for city in weather_data:
        client.sendall((city + "\n").encode("utf-8"))

    # Tell the client that there are no more records to receive.
    client.sendall("END\n".encode("utf-8"))


def handle_client(client, address):
    print("Connected to:", address)

    try:
        # Read the request sent by the client.
        with client.makefile("r", encoding="utf-8") as request_file:
            request = request_file.readline().strip()

        if request == "GET_WEATHER":
            print("Sending weather information...")
            send_weather_data(client)
        else:
            client.sendall("INVALID_REQUEST\n".encode("utf-8"))
            print("Received an invalid request.")

    except OSError as error:
        print("A connection error occurred:", error)

    finally:
        client.close()
        print("Connection closed. Waiting for another client...")


def main():
    # Create the server socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allows the server to reuse the port after it is restarted.
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("Weather server is running.")
    print("Waiting for clients...")

    # Keep the server running so multiple students can connect one at a time.
    while True:
        client, address = server.accept()
        handle_client(client, address)


main()
