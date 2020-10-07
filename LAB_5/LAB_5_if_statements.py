# Write a program that asks for your favorite video game. Python's favorite video game is Tetris.
# Use an if statement to check if your favorite game is the same as Tetris.
# If it is, print the message 'Your favorite video game is the same as mine'
# Else, print the message 'We like different video games.'

# Favorite game is Tetris

# question being asked
favorite_game = input('What is your favorite game? ')

# if statement if games are different
if favorite_game.upper() != 'TETRIS':
    print('We like different video games.')
# if games are the same 'Tetris/tetris' print the same as Python's
else:
    print('Your favorite game is same as mine.')