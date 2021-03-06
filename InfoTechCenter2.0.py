# Code Name - Hornet

import random
from time import sleep #Print to one line with time delay between prints

# Welcome Branch
print("\033[1;34;40m Welcome to Hornets InfoTechCenter\n")

sleep(1)

print("\033[1;37;40m Hornet's Operating System Booting Up\n")

sleep(2)

# Gas Level Function
# Gas Branch
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)

    return currentGasLevel


#Variable calls the value of the gasLevelGauge Function.
gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the comparative operator == Equal To in order to display gas level messages.
def gasLevelAlert():
    gasStations = ["Shell", "BP", "Citgo", "Circle K", "Mobil", "Speedway", "Marathon", "Love's", "Meijer", "Costco", "Sunoco"]
    miles = round(random.uniform(1,25), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING***\n YOUR TANK IS EMPTY\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\n YOUR TANK IS LOW\n The closest service station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away!")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a Quarter Tank of gas left\n Start planning to travel to a service station")
    elif gasLevelIndicator == "Half Tank":
        print("You have half a tank of gas left\n You have 125 more miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your have three quarters of a tank of gas left\n You have 157 more miles till empty")
    else:
        print("You have a full tank of gas, Congratulations\n You have 250 miles left\n")


# call Functions Here
gasLevelAlert()