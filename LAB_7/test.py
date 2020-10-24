guests_list = []

while True:
    name = input('Enter in the names of the guest: ')
    if not name:
        break

    if name.title() in guests_list:
        print('That name is already part of the list.')
    else:
        guests_list.append(name.title())

    print(guests_list)

for number, name in enumerate(guests_list): # LAB: TUPLE UNPACKING ~ INDIVIDUAL VALUES
    print('Guest ' f'{number+1}')
    print(name)


