# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)

        for rowno, row in enumerate(rows):
            record = dict(zip(header, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:    
                print(f'Row {rowno}: Bad row: {row}')

        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total Cost:', cost)

    