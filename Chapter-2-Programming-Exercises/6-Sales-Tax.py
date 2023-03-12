# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax. Assume the
# state sales tax is 5% and the county sales tax is 2.5%. The program should
# display the amount of the purchase, the state sales tax, the country sales
# tax, the total sales tax, and the total of the sale(which is the sum of the
# amount of purchase plus the total sales tax).

# Ask user to input data
purchase_amount = input("Please enter the amount of purchase: ")

# Assign values to variables
state_sales_tax = .05
county_sales_tax = .025
total_sales_tax = state_sales_tax + county_sales_tax

# Calculate & display
print(f"Amount of Purchase: ${purchase_amount}")
print(f"State Sales Tax: ${float(purchase_amount * state_sales_tax)}")
print(f"County Sales Tax: ${float(purchase_amount * state_sales_tax)}")
print(f"Total Sales Tax: ${float(total_sales_tax * purchase_amount)}")
print(f"Grand Total: ${float(purchase_amount + total_sales_tax)}")