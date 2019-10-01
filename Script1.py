'''
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 10/01/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Prompt the user to provide the latitude and longitude for the location they would like to check the forecast for
lat = input("Type in the value of the latitutde of the place you want to get the forecast for in decimal degrees; to four decimal places; in quotations, e.g. '42.2634', then press enter: ")
lon = input("Type in the value of the longitude e.g. '-71.8022' then press enter: ")

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# add in spaces between words where there should be spaces
# Print list to remove unicode characters
for day in forecast:
  day = day.replace("Night", " Night")
  day = day.replace("Chance", "Chance ")
  day = day.replace("High", " High")
  day = day.replace("Low", " Low")
  day = day.replace("Likely", " Likely")
  day = day.replace("then", "then ")
  print day
