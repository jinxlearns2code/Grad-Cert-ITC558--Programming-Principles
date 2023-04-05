# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is
# outside the range of 1 through 10, the program should display an error message.

# Prompt the user to enter a number
num = int(input("Please enter a number from 1 - 10: "))

# Values
one = "I"
two = "II"
three = "III"
four = "IV"
five = "V"
six = "VI"
seven = "VII"
eight = "VIII"
nine = "IX"
ten = "X"

# Display
if 1 <= num <= 10:
    print("----------------------")
    print("Number \t Roman Numeral")
    print("----------------------")

# if elif statements
if num == 1:
    print(f"{num:^5} \t {one:^12}")
elif num == 2:
    print(f"{num:^5} \t {two:^12}")
elif num == 3:
    print(f"{num:^5} \t {three:^12}")
elif num == 4:
    print(f"{num:^5} \t {four:^12}")
elif num == 5:
    print(f"{num:^5} \t {five:^12}")
elif num == 6:
    print(f"{num:^5} \t {six:^12}")
elif num == 7:
    print(f"{num:^5} \t {seven:^12}")
elif num == 8:
    print(f"{num:^5} \t {eight:^12}")
elif num == 9:
    print(f"{num:^5} \t {nine:^12}")
elif num == 10:
    print(f"{num:^5} \t {ten:^12}")
else:
    print("The number you entered is out of range. Please enter a number from 1 to 10.")
