# pcost.py
#
# Exercise 1.27
import csv

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
    
cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost)

    