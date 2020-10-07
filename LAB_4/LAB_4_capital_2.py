# Question given the amounts of attempts
answer = input('What is the state capital of Wisconsin? ')
# If 0 and not 1 will count the first '0' answer as not an attempt
attempts = 1
is_correct = False

# Attempts is less than 3 (including first answer is an attempt) if not correct, loops the question to repeat
while (attempts < 3) and answer.upper() != 'MADISON':
    attempts += 1
    print('Error - incorrect answer, try again')
    answer = input('What is the state capital of Wisconsin? ')
    if answer.upper() == 'MADISON':
        break
    else:
        continue
# print if all attempts have been used
if answer.upper() == 'MADISON':
    is_correct = True
    print('You used ' + str(attempts) + ' out of 3 attempt(s) ')
else:
    print('You used all ' + str(attempts) + ' attempt(s) ')
# WHEN ANSWER IS RIGHT PRINT CORRECT
if is_correct == True:
    print('Correct!')
# STATE THE CORRECT ANSWER- Madison
else:
    print('The correct answer was Madison.')


