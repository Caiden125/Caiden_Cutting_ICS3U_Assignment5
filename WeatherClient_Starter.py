# WeatherClient.py
# World Weather Station
#
# Run WeatherServer.py first.
# Your job is to complete the functions in this -
# program so it can organize, search, filter, and display weather -
# information received from the server.
# 1. Connect to the weather server.
# 2. Request and receive the weather information.
# 3. Organize the information into a list.
# 4. Let the user search, filter, and view weather information.

import socket

SERVER_HOST = "127.0.0.1" #Dont change this
SERVER_PORT = 12345 #You might need to change this port number


def connect_to_server():
    """
    -------------------------------------------------------
    Connects to the weather server and retrieves the weather information.
    -------------------------------------------------------
    Parameters:
       None
    Returns:
       weather_data - All weather records received from the server
       as one string (str).
    -------------------------------------------------------
    """

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    client.sendall("GET_WEATHER\n".encode("utf-8"))

    weather_data = ""

    with client.makefile("r", encoding="utf-8") as response_file:
        for line in response_file:
            line = line.strip()

            if line == "END":
                break #DO NOT USE BREAK ANYWHERE IN YOUR CODE!!

            weather_data = weather_data + line + "\n"

    client.close()

    return weather_data



def process_weather_data(data):
    """
    -------------------------------------------------------
    Organizes the received weather information into a list of cities.
    -------------------------------------------------------
    Parameters:
       data - Weather information received from the server,
       with each city separated by a new line (str).
    Returns:
       cities - A list containing the weather information
       for each city. Each city is stored as a list containing
       the city, country, coordinates, temperature in Celsius,
       and temperature in Fahrenheit (list).
    -------------------------------------------------------
    """

    pass


def display_all_cities(cities):
    """
    -------------------------------------------------------
    Displays the weather information for every city.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the weather information
       for each city (list).
    Returns:
       None
    -------------------------------------------------------
    """

    pass


def search_city(cities):
    """
    -------------------------------------------------------
    Searches for a city and displays its weather information.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the weather information
       for each city (list).
    Returns:
       None
    -------------------------------------------------------
    """

    pass


def find_hottest_city(cities):
    """
    -------------------------------------------------------
    Finds and displays the city with the highest temperature in Celsius.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the weather information
       for each city (list).
    Returns:
       None
    -------------------------------------------------------
    """

    pass


def filter_cities(cities):
    """
    -------------------------------------------------------
    Displays cities with temperatures above a user-selected value.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the weather information
       for each city (list).
    Returns:
       None
    -------------------------------------------------------
    """

    pass


def display_menu():
    """Display the program menu."""
    print("\n===== WORLD WEATHER STATION =====")
    print("1. Display all cities")
    print("2. Search for a city")
    print("3. Find the hottest city")
    print("4. Filter cities by temperature")
    print("5. Exit")


def main():
    # Step 1: Connect to the server and get the weather information.
    weather_data = connect_to_server()

    # Step 2: Organize the received information into a list.
    cities = process_weather_data(weather_data)

    # Step 3: Keep showing the menu until the user chooses to exit.
    choice = ""

    while choice != "5":
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_cities(cities)
        elif choice == "2":
            search_city(cities)
        elif choice == "3":
            find_hottest_city(cities)
        elif choice == "4":
            filter_cities(cities)
        elif choice == "5":
            print("Thanks for using the World Weather Station!")
        else:
            print("Please enter a number from 1 to 5.")


# Start the program.
main()
