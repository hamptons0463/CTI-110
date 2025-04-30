#Name Stephanie Hampton
#Date 02/16/2025
#Project P2Lab2
#Work with Dictionaries

#create an empty dictionary named cars
cars = {"Camero":18.21, "Prius":53.36, "Model S":110, "Silverado":26}

#Create a list of the keys in the dictionary
keys = cars.keys()

#view content
print()
print(keys)

#get one of the keys from the user
print()
user_input = input("Enter a vehicle to see it's MPG: ")

##with user_input holding the key, we want back the value
print()
print(f"The {user_input} gets {cars[user_input]} mpg.")

##Prompt the user to enter how many the miles they will drive the vehicle
print()
miles_driven = float(input(f"How many miles will you drive the {user_input}? "))

#calculate gallons of gas needed to drive milage given
print()
num_gallons = miles_driven/cars[user_input]

print()
print(f"{num_gallons:.2f} gallon(s) of gas are needed to drive the {user_input} {miles_driven} miles.")
print()

