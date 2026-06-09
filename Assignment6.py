# Assignment 6
import requests

API_KEY = "YOUR_API_KEY"
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
print(response)
# Explore other free APIs similarly using requests library.
