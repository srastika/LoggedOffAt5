from rich.console import Console
from rich import print
from constants import weather_icons
from rich import print

# This method prints the full report of the weather
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
    #weather description
    description = report[0]['description']

    print_city_name(data['name'])
    print_temperature(int(float(temperature) - 273.15))
    print_pressure(pressure)
    print_weather_description(description)

def print_weather_description(description):
    """This method prints the weather description in a beautiful way"""
    #get the key that matches description and print result in format print(f"Weather Report: [weather_icons[description][color] weather_icons[description][color]]{description}[/weather_icons[description][color] weather_icons[description][color]] {weather_icons[description]}")
    if description.lower() in weather_icons.keys():
        color=weather_icons[description.lower()]["color"]
        print(f"Weather Report: [bold {color}]{description}[/bold {color}] {weather_icons[description.lower()]['icon']}")

def print_city_name(city_name):
    """This method prints the city name in a beautiful way"""
    console = Console()

    # Create a Unicode string with larger characters
    larger_city_name = ""
    for char in city_name:
        larger_char = char.upper()
        if larger_char.isalpha():
            larger_char = chr(ord(larger_char) + 119743)  # Add offset for larger characters
        larger_city_name += larger_char
    # add space between each character
    larger_city_name = " ".join([char.upper() if char.isalpha() else char for char in city_name])

    # Print the larger city name
    console.print(f"[bold spring_green3]{larger_city_name:^30}[/bold spring_green3]")

def print_temperature(temperature):
    """This method prints the temperature in a beautiful way"""
    #if temperature is less that 10 print in blue , if between 10 and 20 print in yellow , if greater than 20 and less that 30 print in orange , else print in red
    if temperature < 10:
        color="blue"
    elif temperature >= 10 and temperature < 20:
        color="yellow"
    elif temperature >= 20 and temperature < 30:
        color="orange"
    else:
        color="red"
    print(f"Temperature: [bold {color}]{temperature}°C[/bold {color}]")

#similar to the above create function for pressure
def print_pressure(pressure):
    """This method prints the pressure in a beautiful way"""
    #if pressure is less that 1000 print in blue , if between 1000 and 2000 print in yellow , if greater than 2000 and less that 3000 print in orange , else print in red
    if pressure < 1000:
        color="blue"
    elif pressure >= 1000 and pressure < 2000:
        color="yellow"
    elif pressure >= 2000 and pressure < 3000:
        color="orange"
    else:
        color="red"
    print(f"Pressure: [bold {color}]{pressure} hPa[/bold {color}]")
