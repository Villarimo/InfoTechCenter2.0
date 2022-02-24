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
        print("\n VRS has changed your alarm 30 minutes earlier\n based on the NWS", weatherAlert)
        print(" VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\n VRS has changed your alarm 15 minutes earlier\n based on the NWS", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\n VRS has changed your alarm 10 minutes earlier\n based on the NWS", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\n VRS has changed your alarm 5 minutes earlier\n based on the NWS", weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "fog":
        print("\n VRS has changed your alarm 10 minutes earlier\n based on the NWS", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\n weather is", weatherAlert, "Let's GOOOOOOOOOOOOOOOOOOOOOO")
        print("VRS will only allow your car to go 120MPH")

vehicleResponseSystem()