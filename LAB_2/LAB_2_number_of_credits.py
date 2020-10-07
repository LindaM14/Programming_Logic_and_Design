# Number of Credits Write a program that asks for your name,
# and the number of credits you are taking this semester.
# Print a message with this information, for example,
# 'Sam is taking 7 credits this semester' or 'Miriam is taking 9 credits this semester'

# first string value - name
name = input('What is your name?')

# 'second string- number of credits taking this semester
credits = int(input('How many credits are you taking? '))

print(name +' is taking ' + str(credits) + ' credits this semester')