# Weather Branch

import random


def weather():
    weatherForecast = ["Ice", "Snowy", "Raining", "Windy", "Fog", "Clear"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Calling weather function to determine weather
weatherAlert = weather()

print(weatherAlert)