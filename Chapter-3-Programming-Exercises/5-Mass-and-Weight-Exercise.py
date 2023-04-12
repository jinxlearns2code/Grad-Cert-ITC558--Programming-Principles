# Write a program that asks a user to enter an object's mass, then calculates its weight.
# If the object weighs more than 500 newtons, display a message indicating that it is too heavy.
# If the object weighs less than 100 newtons, display a message indicating that it is too light.

# Prompt user to input data
mass = float(input("Please enter an object's mass to calculate its weight: "))

# Calculate
weight = mass * 9.8

# Conditionals
if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")
else:
    print("Invalid number.")