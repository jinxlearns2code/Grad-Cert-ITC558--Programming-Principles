# The area of a rectangle's length is times its width.
# Write a program that asks for the length and width of
# two rectangles. The program should tell the user which
# rectangle has the greater area, or if the areas are
# the same.

# Ask user to input details
length1 = float(input("Please enter rectangle 1's length: "))
width1 = float(input("Please enter rectangle 1's width: "))
length2 = float(input("Please enter rectangle 2's length: "))
width2 = float(input("Please enter rectangle 2's width: "))

# Calculation
rectangle1_area = length1 * width1
rectangle2_area = length2 * width2

# Display output
print("")
if rectangle1_area > rectangle2_area:
    print("Rectangle 1 has the greater area.")
elif rectangle2_area > rectangle1_area:
    print("Rectangle 2 has the greater area.")
else:
    print("Both areas are equal.")