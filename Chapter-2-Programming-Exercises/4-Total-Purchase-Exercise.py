# A customer in the store is purchasing five items.
# Write a program that asks for the price of each item,
# then displays the subtotal of the sale, the amount
# of sales tax, and the total. Assume the sales tax is 7%.

# Ask user to input values
first_item = float(input("Enter the price: "))
second_item = float(input("Enter the price: "))
third_item = float(input("Enter the price: "))
fourth_item = float(input("Enter the price: "))
fifth_item = float(input("Enter the price: "))

# Constant values
sales_tax = .07

# Calculation
gross_total = first_item + second_item + third_item + fourth_item + fifth_item
total_sales_tax = gross_total * sales_tax
grand_total = gross_total + total_sales_tax

# Display output to the user
print(f"Subtotal: ${gross_total: .2f}")
print(f"GST 7%: ${total_sales_tax: .2f}")
print(f"Your total: ${grand_total: .2f}")
