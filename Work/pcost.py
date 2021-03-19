# pcost.py
#
# Exercise 1.27
total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    hearder = next(f)
    
    for line in f:
        row = line.split(',')
        amount = row[1]
        cost = row[2]
        total_cost += int(amount) * float(cost)

print('Total Cost:', total_cost)
    
    