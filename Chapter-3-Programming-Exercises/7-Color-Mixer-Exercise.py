# Design a program that prompts the user to enter the names of two primary colors to mix.
# If the user enters anything other than "red", "blue", or "yellow", the program should
# display an error message. Otherwise, the program should display the name of the secondary
# color that results.

# Ask user for input
color1 = input("Please enter a color. Choose one from red, blue, or yellow: ")
color2 = input("Please enter another color. Choose one from red, blue, or yellow: ")

# Display output
if color1 == "red" and color2 == "red":
    print(f"{color1} + {color2} = red")
elif color1 == "blue" and color2 == "blue":
    print(f"{color1} + {color2} = blue")
elif color1 == "yellow" and color2 == "yellow":
    print(f"{color1} + {color2} = yellow")
elif color1 == "red" and color2 == "blue":
    print(f"{color1} + {color2} = purple")
elif color1 == "blue" and color2 == "red":
    print(f"{color1} + {color2} = purple")
elif color1 == "blue" and color2 == "yellow":
    print(f"{color1} + {color2} = green")
elif color1 == "yellow" and color2 == "blue":
    print(f"{color1} + {color2} = green")
elif color1 == "red" and color2 == "yellow":
    print(f"{color1} + {color2} = orange")
elif color1 == "yellow" and color2 == "red":
    print(f"{color1} + {color2} = orange")
else:
    print("Error! Please choose a color (red, blue, or yellow).")