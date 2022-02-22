import random

# Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)
    return currentGasLevel

# Create If-ELIF-ELSE statements using comparative operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
         print("***WARNING***\n You have run out of gas\n Calling Emergency Contact")


gasLevelAlert()