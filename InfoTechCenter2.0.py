# Weather Branch

import random


def weather():
    weatherForecast = ["Icy", "Snowy", "Raining", "Windy", "Fog", "Clear"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Calling weather function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("Weather is Icy\n VRS has changed you alarm 30 minutes earlier\n based on the NWS", weatherAlert)
        print(" VRS will only allow your car to go 30MPH")