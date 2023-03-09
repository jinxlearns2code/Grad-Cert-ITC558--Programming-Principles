# Write a program that displays the following information:
# Name, address, telephone number, college major

# Ask user to input details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your address starting with the city: ")
state = input("State: ")
zip_code = input("Zip Code: ")
college_major = input("What's your college major? ")

# Display the personal info to user
print(f"Name: {first_name + ' ' + last_name}")
print(f"Address: {city + ', ' + state + ' ' + zip_code}")
print(f"College Major: {college_major}")
