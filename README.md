<p align="center">
  <a href="" rel="noopener">
 <img src="https://i.imgur.com/AZ2iWek.png" alt="Project logo"></a>
</p>
<h3 align="center">Weather Script using Github Co-Pilot 🤖</h3>

<div align="center">

[![Hackathon](https://img.shields.io/badge/hackathon-name-orange.svg)]([http://hackathon.url.com](https://www.techgig.com/codegladiators/github-copilot-hackathon?solve=1))
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---


## 🧐 Brief Summary of Project <a name = "problem_statement"></a>
The Weather Forecasting Tool is a command-line application that allows users to retrieve the current weather forecast for a specific city. The tool leverages the OpenWeatherMap API to fetch weather data and uses Python for data parsing and error handling. With the assistance of GitHub Copilot, the project incorporates text-to-speech support to enhance accessibility.

The application takes a city's name as input and sends a request to the OpenWeatherMap API to retrieve the weather data for that city. GitHub Copilot assists in generating code snippets and suggestions for making API calls, handling API responses, and parsing the returned data.

Once the weather data is obtained, the application parses it to extract relevant information such as temperature, humidity, wind speed, and weather conditions. This parsing is done with the help of GitHub Copilot, which provides suggestions and code snippets for efficient data extraction and manipulation.

To enhance accessibility, the Weather Forecasting Tool incorporates text-to-speech support. This feature allows users with visual impairments or those who prefer auditory information to listen to the weather forecast instead of reading it. GitHub Copilot assists in implementing the necessary code for text-to-speech functionality, including converting the weather forecast text to speech and playing it back to the user.

Overall, this project showcases how GitHub Copilot can accelerate the development process by providing intelligent code suggestions and automating repetitive tasks. It demonstrates the integration of an external API, data parsing, error handling, and the implementation of text-to-speech support for better accessibility.

## 💡 Business Challenge /Use Cases <a name = "idea"></a>

Provide a reliable and efficient weather forecasting tool within a command-line interface
Text to speech support allowing users with visual impairments or those who prefer auditory information to listen to the forecast
Clear and organized overview of the weather information. 
Fetch essential weather data such as temperature , humidity, pressure , and conditions




## ⛓️ Proposed Solution <a name = "limitations"></a>


### Workflow:

- User enters the city name as input in the command line
- Tool sends a request to the OpenWeatherMap API for weather data
- API response is received and parsed using Python [GitHub Copilot suggestions made parsing and error handling easier]
- Extracted weather information is displayed to the user in a user-friendly format
- Text to speech support for the extracted weather information is also integrated within the tool



### Tool Features:

- Command-Line Interface
- Current Weather Forecast
- OpenWeatherMap API Integration: Leverages OpenWeatherMap API for weather data retrieval
- Python Data Parsing: Parses the API response using Python for data extraction
- GitHub Copilot Assistance: Utilizes GitHub Copilot for API usage, data parsing, and error handling



## 🚀 Future Scope <a name = "future_scope"></a>

- Multilingual and regional language support using azure services
- Enhance User Interface: Consider building a graphical user interface (GUI) for broader user accessibility

  

### Installing

A step by step series of examples that tell you how to get a development env running.
- Clone the repository from GitHub.
- Install the required dependencies. Example: ```pip install -r requirements.txt```
- Create a free account on WeatherAPI.com and obtain an API key. Paste the API Key in the .env file. Example: Inside .env ```API_KEY=<your-api-key>```
- Run the command-line tool and provide the name of the city for which you want to retrieve the weather forecast.
- cd into the weather_forecasting folder ```cd weather_forecasting```
- python weather_forecast.py <city-name> Example: ```python -m weather_forecast.py London```


## ✍️ Authors <a name = "authors"></a>

- [@Harmanjit Singh](https://github.com/harmanjit14)
- [@Srastika Shetty](https://github.com/srastika)


