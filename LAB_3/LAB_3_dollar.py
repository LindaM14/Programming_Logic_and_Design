# Do you have a dollar?
# Write a program that asks the user how many cents (penny coins) they have.
# If they have less than a dollar's worth of cents, print the message 'you have less than a dollar'.
# If they have exactly 100 cents, print the message 'you have exactly one dollar'
# If they have more than 100 cents, print the message 'you have more than one dollar'
# (Bonus question, +3 points: extend your program to check if the user has an exact number of cents in pennies,
# for example 100 or 300 or 700 pennies. Print a message if so. Hint: look up the modulo % operator.)

# line 100 pennies equal a dollar
pennies_in_a_dollar = 100

# how many pennies/cents does said user have when asked question
pennies = int(input('How many cents do you have? '))

# IF exact a 100 pennies/cents print user has exactly 1 dollar
if pennies == pennies_in_a_dollar:
    print('You have exactly one dollar ')
# IF less than 100 pennies/cents state user has less
elif pennies < pennies_in_a_dollar:
    print('You have less than one dollar ')
# IF more than 100 pennies/cents state user has more
elif pennies > pennies_in_a_dollar:
    print('You have more than one dollar ')

# 100/10 = 10 (no remainder)
# 100/10 = 9 remainder 1
    remainder = pennies %100
    print(remainder)