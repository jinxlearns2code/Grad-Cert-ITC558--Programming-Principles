# Write a program that asks the user for the number of males and the number of females
# registered in a class. The program should display the percentage of males and females
# in the class.

# Declare variables and assign initial value.
male = 0
female = 0
total_students = 0
keep_going = 'y'

# Initialise while loop and prompt user to enter the number of students.
while keep_going == 'y':
    male = int(input('Please enter the number of male students in the class: '))
    female = int(input('Please enter the number of female students in the class: '))

# Computation.
    total_students = male + female
    male_percentage = (male / total_students) * 100
    female_percentage = (female / total_students) * 100

# Display output to user.
    print('')
    print(f'The class consists of {male_percentage: .2f}% male students and {female_percentage: .2f}% female students.')
    print(f'There are {total_students} students in the class.')

# Prompt the user if they would like to do another calculation.
    print('')
    keep_going = input('Would you like to do another calculation? Please enter "y" if Yes and "n" if No: ')

# End the program.
print('')
print('Have a nice day.')