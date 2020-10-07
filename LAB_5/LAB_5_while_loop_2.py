# Write a program that asks the user for a 4-letter department code,
# for example ENGL or MATH or ITEC or SPAN or WEBI.
# Use a while loop to validate that the code is exactly 4 letters. If it is, print a 'thank you for the data' message.

# Question being asked
department_code = input('Enter 4-letter department code: ')

# While loop for if its more than 4 to repeat the question until code is 4
while len(department_code) != 4:
    print('Error -- a valid department code is 4-letters, try again')
    department_code = input('Enter 4-letter department code: ')

# print message that it was 4 letters exactly
print('Thank you for the 4-letter code')