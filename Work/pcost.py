# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0
    try:
        with open(filename, 'rt') as f:
            hearder = next(f)

            for line in f:
                row = line.split(',')
                amount = row[1]
                cost = row[2]
                total_cost += int(amount) * float(cost)
            
            return total_cost
        
    except ValueError:
        print("Error!")
    
cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost)

    