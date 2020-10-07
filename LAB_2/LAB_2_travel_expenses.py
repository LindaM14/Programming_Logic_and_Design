# Travel Expenses Write a program that calculates the amount of money spent on bus fares last month.
# Ask the user for the number of times they rode the bus last month
# Ask the user for the cost of one bus ride
# Multiply these numbers to calculate the total cost of riding the bus.
# Print the number of rides, the cost of one bus ride, and the total cost for the user.
# For this problem, you can ignore transfers, and rush-hour fares, and just assume every bus ride costs the same.
# Example output would look like this:
# 'You rode the bus 8 times last month. One bus ride costs $2. Your total cost was $16'

# first string value - # times they rode the bus
items_sold = int(input('How many times did you ride the bus last month? '))

# second string value - $ of one bus ride
unit_price = float(input('How much does one bus ride cost? '))

# third string value - multiple #1 & #2 string to figure out total riding the bus
total = items_sold * unit_price

# fourth string value - # of rides, cost and total cost
print()
print('Number of Rides: ' + str(items_sold))
print('Price per ride: $' + str(unit_price))
print('Total Cost: $' + str(total))

