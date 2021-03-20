# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    try:
        with open(filename) as f:
            rows = csv.reader(f)
            hearder = next(rows)

            for row in rows:
                amount = row[1]
                cost = row[2]
                total_cost += int(amount) * float(cost)
            
            return total_cost
        
    except ValueError:
        print("Error!")

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total Cost:', cost)

    