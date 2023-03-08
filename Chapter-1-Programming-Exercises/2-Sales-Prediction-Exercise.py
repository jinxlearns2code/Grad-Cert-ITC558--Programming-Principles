# Write a program that asks the user to enter the projected
# amount of total sales, then displays the profit that will
# be made from that amount.

# Using 23% of total sales as average annual profit
total_sales = float(input("Enter the projected amount of total sales for the year: "))
annual_profit_percent = .23

# Display the profit
print(f"Your projected annual profit is ${total_sales * annual_profit_percent:.2f}.")
