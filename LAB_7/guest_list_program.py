# P1. 1 creating empty list
import random
guests_list = []
people_who_won_prizes = []
total_guests = 0

# Pt. 2 Loop for name of guests - when done hitting enter that ends the loop - rejecting duplicates
while True:
    name = input('Enter in the names of the guest: ')
    if not name:
        break

    if name.title() in guests_list:
        print('That name is already part of the list.')
    else:
        guests_list.append(name.title())
        total_guests += 1

    print(guests_list)

# Pt. 3 Print all of the names. Use enumerate() to print a numbered list.

for number, name in enumerate(guests_list): # LAB: TUPLE UNPACKING ~ INDIVIDUAL VALUES
    print('Guest ' f'{number+1}')
    print(name) #LAB: can you fix to be more user friendly; Ex. 'Guest 1: Andy'

# Pt. 4Ask the user if they would like to delete any names.
# ^ Use a while loop so the user can delete as many names as needed.
# ^ You can either use remove to delete by name, or pop to delete by index.
# ^ You can decide what the user should do to end this loop.



def numbered_list():
    for number, name in enumerate(guests_list, 1):
        print(number,'.' + name, sep= '',end= ' ')
        print()



# OPTION 1 - remove by value or name
while True:
    print('Here\'s the list of names: ' + str(guests_list))
    remove_name = input('Enter the name you want to remove: ')

    if not remove_name:
        break

    if remove_name in guests_list:
        guests_list.remove(remove_name)
        total_guests = total_guests - 1
    else:
        print('That name is not in the list. Please try again')

# PT 5. enumerated again but not like #3
    numbered_list()
# # PT 6. Random prizes to different guests //ask user then how many//use RANDOM fuction
random_prize = 0
how_many_prizes = int(input('How many prizes should be given out? '))
while random_prize < how_many_prizes:
    prizes = random.choice(guests_list)

    if prizes.title() in guests_list:
        print('That name has already won a prize.')
        break
    else:
        people_who_won_prizes.append(prizes.title())


# PT 7. The total number of guests, All the guests as a numbered list  (use the function described in part 5), The names of the guest(s) who will be given a prize
print('Total guests: ')
print(total_guests)
print(numbered_list())
num = 1
for num in range(len(guests_list)):
    print(guests_list[num])
    num += 1






