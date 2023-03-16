# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar, 1 cup of butter, 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients.
# Write a program that asks the user how many cookies he or she wants
# to make, then displays the number of cups of each ingredient needed
# for the specified number of cookies.

# Declare variables
sugar_fixed = 1.5
butter_fixed = 1
flour_fixed = 2.75
cookies_fixed = 48

# User to input desired number of cookies
user_preference = int(input("Please enter the desired number of cookies: "))

# Computation and display
sugar_temp = sugar_fixed / cookies_fixed
butter_temp = butter_fixed / cookies_fixed
flour_temp = flour_fixed / cookies_fixed
print(f"You will need the following ingredients to make {user_preference} cookies:")
print(f"1.{sugar_temp * user_preference: .2f} cup/s of sugar")
print(f"2.{butter_temp * user_preference: .2f} cup/s of butter")
print(f"3.{flour_temp * user_preference: .2f} cup/s of flour")