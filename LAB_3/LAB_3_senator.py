#Can you be a senator?
# Article I, Section 3 of the Constitution sets out three qualifications for senators:
# (1) they must be at least 30 years old,
# (2) they must have been citizens of the United States for at least the past nine years, and

# Write a program that asks the user four questions:
# the state they want to be a senator in,
# their age, as an int number,
# if they have been a citizen of the US for at least 9 years,
# the state they currently live in. (to be eligible, this needs to be the same as the state they want to be the senator of).

# Use an if statement or statements to check if they are eligible or not.
# You will need to check if the age >= 30, and if the years of US citizenship >= 9 and
# if the state they want to be a senator == state the currently live in.
# Print an appropriate message telling the user if they are eligible to be a senator or not.

old_enough = False
is_citizen = False
can_be_a_senator = False
same_location = False

# state they want to be a senator in
senator_state = input('What state would you want to be a senator in? ')

# age as a INT
age = int(input('What is your age? '))
if age >= 30:
    old_enough = True

# yrs of citizenship (9)
citizen = int(input('How long have you been a US Citizen? '))
if citizen >= 9:
    is_citizen = True

# state living at // (can't be a senator from a different state)
state_they_currently_live_in = input('What state do you currently live in? ')

if senator_state == state_they_currently_live_in:
    same_location = Truecl

# confirm requirements
if (old_enough) and (is_citizen) and (same_location):
    can_be_a_senator = True

if can_be_a_senator == True:
    print('You are eligible to be a senator!')
else:
    print('You are not eligible to be a senator.')

