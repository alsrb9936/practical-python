# pcost.py
#
# Exercise 1.27
total_cost = 0
colum = []

with open('Data/portfolio.csv', 'rt') as f:
    hearder = next(f)
    
    for line in f:
        colum = line.split(',')
        total_cost = total_cost + int(colum[1]) * float(colum[2])

print('Total Cost:', total_cost)
    
    