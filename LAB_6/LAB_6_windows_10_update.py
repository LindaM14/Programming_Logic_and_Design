# When installing Windows 10, a user can either wipe everything from their computer and do a clean install.
# Or if their computer meets system requirements, the user can upgrade to Windows 10 without erasing their current operating system.
#
# To do the upgrade, according to Microsoft, a computer needs to have at least 1GB of memory, and at least 1GHz processor,
# and either Windows 7 or Windows 8 currently installed.   All three requirements must be met.
#
# Write a program that asks the user for
#
# The current memory in their computer, in GB.  (For example, a user with 8GB of memory would enter 8)
# The current processor speed, in GHz. (For example, a user with a 2.6GHz processor should enter 2.6)
# The name of their current operating system. (For example, a user could enter Windows 8 or Windows 7 or Windows XP)
# Write a can_upgrade function that takes three arguments, the amount of memory, the processor speed, and current operating system.
#
# In can_upgrade, use conditions to figure out if the user's computer can be upgraded to Windows 10 or not.
# Your function should return one of the Boolean values True (if the computer can be upgraded) or False (if it can't be upgraded).
#
# Call your can_upgrade function from main(), and use the return value to print a message to the user telling them if they can, or can't, upgrade.

def can_upgrade(memory, processor_speed, os):
    reply_one = int(input('What is memory in GB on your computer? '))
    reply_two = int(input('What is your current processor speed in GHz? '))
    reply_three = input('What is your current operating system? ')

    if (reply_one >= memory) and (reply_two >= processor_speed) and (reply_three == os or reply_three == 'Windows 8'):
        return True
    else:
        return False

def main():
    function = can_upgrade(1, 1, 'Windows 7')
    if function == True:
        print('You can upgrade to Win10! ')
    else:
        print('You cannot upgrade to Win10. ')

main()