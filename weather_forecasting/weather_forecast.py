import sys
import pandas as pd
import re
import os
from dotenv import load_dotenv
import requests
# fucntion to accept city name from user command line
# also add error handling for invalid city


"""Global Variables"""
load_dotenv()
reg = r"^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$"
regex = re.compile(reg, re.IGNORECASE)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("API_KEY")


def validate_city():
    """If we want to use pandas to analyse the city we can use this"""
    df = pd.read_csv("allCities/worldcities.csv")
def print_report(data):
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # weather report
    report = data['weather']
    print(f"{city_name:-^30}")
    print(f"Temperature: {int(float(temperature)-273.15)} C")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")

def get_weather(city_name):
    URL = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        print_report(data)
    else:
        # showing the error message
        print("Error in the HTTP request")


def validate_argument():
    """This method validates inputs from user, If multiple inputs are 
    detected it appends all to a single input and If none input is 
    detected it asks user to enter value again"""
    city_name = ""
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            city_name += str(sys.argv[i]) + " "
    else:
        print("No City Input Found 😕\n(CTRL+C to Exit)")
        while (len(city_name) < 1):
            city_name = input("Try Again - Enter City 😃: ")
    return city_name


def get_city_name():
    try:
        city_name = sys.argv[1]
        return city_name
    except:
        print("Invalid City Name")
        sys.exit(1)


# __main__ function that calls get_city_name()
# and prints the weather forecast for the city
if __name__ == "__main__":
    # city_name = get_city_name()
    city_name = validate_argument()
    get_weather(city_name)

