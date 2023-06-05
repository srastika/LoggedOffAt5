import sys
import pandas as pd
import re
import os
from dotenv import load_dotenv
import requests
from print_report import print_report
from weather_next_few_days import get_forecast_next

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


def get_weather(city_name):
    URL = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        print_report(data)
        print()
        get_forecast_next(city_name, API_KEY)
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




# __main__ function that calls validate_argument()
# and prints the weather forecast for the city
if __name__ == "__main__":
    city_name = validate_argument()
    get_weather(city_name)

