# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food, then calculate the
# amounts of an 18 percent tip and 7 percent sales tax. Display each of these amounts
# and the total.

# Ask user to input data
food_charge = float(input("Please enter the amount charged for the food: "))

# Computation and display of data
tip = .18
sales_tax = .07
print(f"Tip 18%: {food_charge * tip: .2f}")
print(f"Sales Tax 7%: {food_charge * sales_tax: .2f}")
print(f"")