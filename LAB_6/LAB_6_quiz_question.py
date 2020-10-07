# Write a function that takes two arguments - a quiz question and the correct answer.
# In your function, you will print the question, and ask the user for the answer.
# If the user gets the answer correct, print a success message.
# Else, print a message with the correct answer.
# Your function does not need to return anything.
# Call your function with two example quiz questions.   Here's some suggestions,
#
# Q: What year did Apollo 11 land on the moon? A: 1969
# Q: Who painted the Mona Lisa? A: Leonardo da Vinci

def quiz(question, answer):
    user_input = input(question)
    if user_input == answer:
        print('Correct! ')
    else:
        print('Incorrect, correct answer was ' + answer)

def main():
    quiz('What year did Apollo 11 land on the moon? ', '1969')
    quiz('Who painted the Mona Lisa? ', 'Leonardo da Vinci')

main()
