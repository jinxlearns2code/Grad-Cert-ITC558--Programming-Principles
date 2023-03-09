# Write a program that asks a user to enter the total square feet in a tract of land
# and calculate the number of acres in a tract.

# Assign values to variables
one_acre = 43560
total_feet = int(input("Enter the total square feet in a tract of land: "))

# Calculate the number of acres
print(f"The total number of acres is: {total_feet / one_acre: .2f} acre/s.")
