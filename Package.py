import requests
from datetime import datetime

from forex_python.converter import CurrencyRates

import json


password = '''
{
    "pass": "41849ba22c12ba5e636760b61f8dd282"
}
'''

data = json.loads(password)

c = CurrencyRates()


print("""
    This is a python program that takes a person’s name, city and annual income, and return to them:
    1) The current weather
    2) The current exchange rate to the dollar (USD)
    3) A decision on whether they can live in St Tropé based on their income converted
""")
st_tropez = 62532

name = input("Please enter your name: ")
income = input("What is your annual income: ")
symbol = input("Please input your currency code (in capital letters): ")
location1 = input("Enter the city name: ")

complete_api_link = f"http://api.openweathermap.org/data/2.5/weather?q={location1}&appid={data['pass']}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid: {}, Please check your City name".format(location1))
else:
    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location1.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')

print("\n")
exchange = c.convert('USD', symbol, income)
print(f"{exchange} this is what you are worth in USD \n")

if exchange >= st_tropez:
    print(f"St Tropez is the place for you {name}")

else:
    print(f"{name} you are too poor for St Tropez")
