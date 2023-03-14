# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax. Assume the
# state sales tax is 5% and the county sales tax is 2.5%. The program should
# display the amount of the purchase, the state sales tax, the country sales
# tax, the total sales tax, and the total of the sale(which is the sum of the
# amount of purchase plus the total sales tax).

# Ask user to input data
purchase_amount = float(input("Please enter the amount of purchase: "))

# Assign values to variables
state_sales_tax = .05
county_sales_tax = .025
combined_sales_tax = state_sales_tax + county_sales_tax
total_sales_tax = combined_sales_tax * purchase_amount

# Calculate & display
print(f"Amount of Purchase: ${purchase_amount: .2f}")
print(f"State Sales Tax: ${purchase_amount * state_sales_tax: .2f}")
print(f"County Sales Tax: ${purchase_amount * county_sales_tax: .2f}")
print(f"Total Sales Tax: ${total_sales_tax: .2f}")
print(f"Grand Total: ${purchase_amount + total_sales_tax: .2f}")