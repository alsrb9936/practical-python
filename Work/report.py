# report.py
#
# Exercise 2.4
import csv
    
def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            temp = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(temp)
            
    return portfolio

def read_prices(filename):
    prices = {}
    
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        
        try:
            for row in rows:
                prices[row[0]] = float(row[1])
        
        except IndexError:
            pass
            
    return prices

def make_report(portfolio, prices):
    report = []
    
    for line in portfolio:
        name = line['name']
        shares = int(line['shares'])
        past_price = float(line['price'])
        change = past_price - prices[name]
        
        temp = (name, shares, prices[name], change)
        report.append(temp)
    
    return report

portfolio_file = 'Data/portfolio.csv'
prices_file = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_file)
prices = read_prices(prices_file)
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
Gain = 0

for i in portfolio:
    portfolio_cost = i['price'] 
    now_cost = prices[i['name']]
    shares = i['shares']
    
    Gain += shares * (now_cost - portfolio_cost)
    
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print(('-' * 10 + ' ') * len(headers))
    
for name, shares, price, change in report:
    price = f'${price:.2f}'
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    
