# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week, where 1 = Monday,
# 2 - Tuesday, and so on. The program should display an error message if the user
# enters a number that is outside the range of 1 through 7.

# Declare a variable
day_of_week = int(input("Please enter a number from 1 - 7: "))

# if elif statement
if day_of_week == 1:
    print("Monday")
elif day_of_week == 2:
    print("Tuesday")
elif day_of_week == 3:
    print("Wednesday")
elif day_of_week == 4:
    print("Thursday")
elif day_of_week == 5:
    print("Friday")
elif day_of_week == 6:
    print("Saturday")
elif day_of_week == 7:
    print("Sunday")
else:
    print("Number is outside of range.")