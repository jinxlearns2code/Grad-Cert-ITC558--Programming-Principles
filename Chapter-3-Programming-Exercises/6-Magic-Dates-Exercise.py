# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
# The program should then determine whether the month times the day equals the year. If so, it should
# display a message saying the date is magic. Otherwise, it should display a message saying the date
# is not magic.

# Ask users to input data
day = int(input("Please enter the day of the month: "))
month = int(input("Please enter the month (in numeric form): "))
year = int(input("Please enter the year (in 2-digit format e.g. 61 instead of 1961): "))

# Calculate
check_magic = day * month

# Display output
if check_magic == year:
    print("The date is magic.")
else:
    print("The date is not magic.")