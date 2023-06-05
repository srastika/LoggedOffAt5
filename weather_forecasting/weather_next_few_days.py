import requests
from  datetime import datetime
from constants import weather_icons
from rich import print
from text_to_speech import speak

BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

def get_formatted_date(timestamp):
    """From timestamp in format yyyy-mm-dd get weekday , month and day"""
    date_object = datetime.strptime(str(timestamp), "%Y-%m-%d")
    weekday = date_object.strftime("%A")
    month = date_object.strftime("%B")
    day = date_object.day
    return f"{weekday} {month} {day}"
    


def get_forecast_next(city_name,API_KEY):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_list = data['list']

        current_date = None
        for forecast in forecast_list[1::]:
            timestamp = forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp).date()

            # Only consider the first entry for each new day
            if forecast_date != current_date:
                current_date = forecast_date
                weather_description = forecast['weather'][0]['description']
                #get weathericon
                print(f"{get_formatted_date(current_date):<25} {weather_icons[weather_description.lower()]['icon']:<20}")
                color=weather_icons[weather_description.lower()]["color"]
                #add color to weather description
                print(f"[bold {color}]{weather_description}[/bold {color}]")
                print()  
                #speak date followed by weather description
                speak(f"{get_formatted_date(current_date)} {weather_description}")      
    else:
        print("Error in the HTTP request")

