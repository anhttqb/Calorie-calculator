import requests
from bs4 import BeautifulSoup

WEATHER_WEB_URL = "https://www.timeanddate.com/weather"


class Temperature:
    """This class is responsible for getting the current temperature
    based on user information of their current living city and country.
    Temperature will be extracted from the timeanddate.com/weather website."""

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def get_temperature(self):
        r = requests.get(f"{WEATHER_WEB_URL}/{self.country}/{self.city}")
        weather_webpage_content = r.text

        soup = BeautifulSoup(weather_webpage_content, 'html.parser')

        current_temp = soup.find_all(class_='h2')[0].text
        return int(current_temp[:2])
