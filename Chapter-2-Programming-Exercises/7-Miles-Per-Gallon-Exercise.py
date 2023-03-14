# A car's miles per gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used.
# It should calculate the car's MPG and display the result.

# Ask user to input data
miles_driven = float(input("Please enter the number of miles driven: "))
gallons_used = float(input("Please enter the gallons of gas used: "))

# Computation and display
print(f"Your car's Miles per Gallon (MPG) is {miles_driven / gallons_used: .2f}.")
