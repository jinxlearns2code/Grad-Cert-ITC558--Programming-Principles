# Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follows: F = 9/5C + 32.
# The program should ask the user to enter a temperature in Celsius, then display
# the temperature converted to Fahrenheit.

# Ask user to input data:
print("-------------------------------------------------------------")
print("This program converts temperature from Celsius to Fahrenheit.")
print("-------------------------------------------------------------")
celsius = float(input("Please enter the temperature in Celsius: "))

# Calculation and display:
fahrenheit = f"{(9 * celsius) / 5 + 32}"
print("")
print(f"{celsius} degrees in Celsius is {fahrenheit} degrees in Fahrenheit.")
