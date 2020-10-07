# Ask for the number of classes you are taking. Save in an integer variable.
# Create an empty string called class_names
# Write a for loop that asks for each class name.
# Add each class name to the class_names string, followed by a '\n' newline character.
# And the end of the loop, print the class_names string.  Here's example output from the program:

# How many classes are you taking? 3
# Enter the name of a class: Programming Logic
# Enter the name of a class: Information Technology Concepts
# Enter the name of a class: Preparing for IT
# Here are your classes:
# Programming Logic
# Information Technology Concepts
# Preparing for IT

# empty strings for class and random class user inputs
class_names = ''
random_class = ''

# how many user inputting are taking
many_classes_taken = int(input('How classes are you taking? '))

# loop for the 'x' amount of classes taken what the names are, to repeat until 'x' of classes are full
for n in range(many_classes_taken):
    name_of_class = str(input("Enter the name of a class: "))
    random_class += name_of_class + '\n'
    class_names += name_of_class + '\n'

# print all class and names
print('Here are your classes:')
print(random_class)


