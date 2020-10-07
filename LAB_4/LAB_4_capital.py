# GOAL: keep making question repeat if question is wrong
answer = input('What is the state capital of Wisconsin? ')

# LOOP: if answer is wrong makes the question be asked again until right then will print correct
while answer.upper() != 'MADISON':
    print('Error - incorrect answer, try again')
    answer = input('What is the state capital of Wisconsin? ')
    if answer.upper() == 'MADISON':
        break
    else:
        continue
print('Correct! the state capital of Wisconsin is Madison.')