import sys
#fucntion to accept city name from user command line
#also add error handling for invalid city name
def get_city_name():
    try:
        city_name = sys.argv[1]
        return city_name
    except:
        print("Invalid City Name")
        sys.exit(1)

#__main__ function that calls get_city_name() 
#and prints the weather forecast for the city   
if __name__ == "__main__":
    city_name = get_city_name()
    print("Weather Forecast for " + city_name + " is Sunny") #hardcoded for now


