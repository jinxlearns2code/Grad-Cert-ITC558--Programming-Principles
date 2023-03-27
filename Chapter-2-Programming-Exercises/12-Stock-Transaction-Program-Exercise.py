# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
# The number of shares that Joe purchased was 2,000.
# When Joe purchased the stock, he paid $40.00 per share.
# Joe paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
# Two weeks later, Joe sold the stock. Here are the details of the sale:
# The number of shares that Joe sold was 2,000.
# He sold the stock for $42.75 per share.
# He paid his stockbroker another commission that amounted to 3 percent of the amount he paid for the stock.

# Write a program that displays the following information:
# The amount of money Joe paid for the stock.
# The amount of commission Joe paid his broker when he bought the stock.
# The amount for which Joe sold the stock.
# The amount of commission Joe paid his broker when he sold the stock.
# Display the amount of money that Joe had left when he sold the stock and paid his broker (both times).
# If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

# Purchase
purchased_shares = float(input("Please enter the number of shares that were purchased: "))
purchase_price = float(input("Please enter the price paid per share: "))
purchase_commission = float(input("Please enter the stockbroker commission in percentage: "))
stockbroker_purchase_commission = (purchased_shares * purchase_price) * (purchase_commission / 100)
total_cost = (purchased_shares * purchase_price) + stockbroker_purchase_commission

# Sell
sold_shares = float(input("Please enter the number of shares that were sold: "))
sell_price = float(input("Please enter the sell price per share: "))
sell_commission = float(input("Please enter the stockbroker commission in percentage: "))
stockbroker_sell_commission = (sold_shares * sell_price) * (sell_commission / 100)
total_sales = (sold_shares * sell_price) - stockbroker_sell_commission

# Calculate profit or loss
net_amount = total_sales - total_cost

# Display output
print("")
print("------------------------------------------------------------------")
print(f"${stockbroker_purchase_commission:,.2f} was paid to the broker when the shares were purchased.")
print(f"${stockbroker_sell_commission:,.2f} was paid to the broker when the shares were sold.")

# if-else to display profit or loss
if net_amount > 0:
    print(f"Profit: ${net_amount:,.2f}")
elif net_amount == 0:
    print("Breakeven")
else:
    print(f"Loss: ${net_amount:,.2f}")

print("------------------------------------------------------------------")