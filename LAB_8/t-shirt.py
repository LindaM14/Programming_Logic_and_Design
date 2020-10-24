# put this in code for average sales
up_arrow = chr(8593)   # ↑
down_arrow = chr(8595)    # ↓

# A t-shirt vendor is working at a week-long event that runs from Monday until Sunday.
days_of_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

daily_sale = {}
# question to ask user to input the amount of tshirt sales from M-F and to print all the sales
for tshirt in days_of_the_week:
    sales = float(input(f'T-shirt sales on {tshirt}: '))
    daily_sale[tshirt] = sales

total_tshirts = sum(daily_sale.values())

# prints the total amount of shirts and average for the values input in values M-F
tshirts = len(daily_sale)
average = total_tshirts / tshirts

print()
print(f'The total sales of T-shirts for the week: {total_tshirts}')
print(f'The average of T-shirt sales for the week: {average}')

# if shirts are greater than or equal to average print ↑ next to value, if less than average print a ↓
for tshirt, sales in daily_sale.items():
    if sales >= average:
         print(f' {tshirt} sales: {sales} {up_arrow}')
    if sales < average:
        print(f' {tshirt} sales: {sales} {down_arrow}')

