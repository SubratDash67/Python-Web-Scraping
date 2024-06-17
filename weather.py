# imports
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import numpy as np

# create geopy object and function for finding long and lat
gn = Nominatim(user_agent="weather-Scraper")


def geolocate(city=None, country=None):
    """
    Inputs city and country, or just country. Returns the lat/long coordinates of
    either the city if possible, if not, then returns lat/long of the center of the country.
    """
    # If the city exists,
    if city:
        try:
            # Geolocate the city and country
            loc = gn.geocode(f"{city}, {country}")
            return (loc.latitude, loc.longitude)
        except:
            return np.nan
    else:
        try:
            loc = gn.geocode(country)
            return (loc.latitude, loc.longitude)
        except:
            return np.nan


# hashmap of all Indian states
states = {
    "AP": "Andhra Pradesh",
    "AR": "Arunachal Pradesh",
    "AS": "Assam",
    "BR": "Bihar",
    "CG": "Chhattisgarh",
    "GA": "Goa",
    "GJ": "Gujarat",
    "HR": "Haryana",
    "HP": "Himachal Pradesh",
    "JK": "Jammu and Kashmir",
    "JH": "Jharkhand",
    "KA": "Karnataka",
    "KL": "Kerala",
    "MP": "Madhya Pradesh",
    "MH": "Maharashtra",
    "MN": "Manipur",
    "ML": "Meghalaya",
    "MZ": "Mizoram",
    "NL": "Nagaland",
    "OR": "Odisha",
    "PB": "Punjab",
    "RJ": "Rajasthan",
    "SK": "Sikkim",
    "TN": "Tamil Nadu",
    "TS": "Telangana",
    "TR": "Tripura",
    "UP": "Uttar Pradesh",
    "UK": "Uttarakhand",
    "WB": "West Bengal",
}

# ask for input from the user and store as variables
resultCity = input("Enter an Indian city: ")
resultState = input("Enter the state: ")
result = geolocate(city=resultCity, country="India")

try:
    lat = result[0]
except:
    print("Error: Input was invalid or does not exist.")
    exit()

if states.get(resultState):
    lon = result[1]
else:
    try:
        if states[resultState]:
            lon = result[1]
    except:
        print("Error: Input was invalid or does not exist.")
        exit()

# Create url for the requested location through string concatenation
# OpenWeatherMap API can be used for getting weather details. Assuming API key is "your_api_key"
api_key = ""
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

# Send request to retrieve the web-page using the get() function from the requests library
response = requests.get(url)
weather_data = response.json()

if response.status_code == 200:
    # Extract weather details
    main = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]

    # Return scraped information
    print(
        f"The Current Weather Conditions in {resultCity}, {resultState} is: {main} ({description})"
    )
    temperature_celsius = temperature - 273.15
    print(f"Temperature: {temperature_celsius:.2f}C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
else:
    print("Error: Could not retrieve weather data.")
